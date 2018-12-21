import time
import json
import os
import subprocess
from datetime import datetime
from hashlib import md5 as hashlib_md5

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection

from .settings import ourfa_args

from .models import (
    Accounts,
    AccountTariffLink,
    Users108,
    Tariffs,
    DiscountPeriods,
    PaymentTransactions,
)


context = {}


def __md5(_str):
    return hashlib_md5(_str.encode()).hexdigest()


def generate_order_idp(login, sum):
    _time = str(int(time.time()))
    return ''.join([login, sum, _time])


def uppercase(_str):
    return _str.upper()


def make_signature(post_attrs, _password):
    Shop_IDP = post_attrs['Shop_IDP']
    Order_IDP = post_attrs['Order_IDP']
    Subtotal_P = post_attrs['Subtotal_P']
    MeanType = ''
    EMoneyType = ''
    Customer_IDP = post_attrs['Customer_IDP']
    Card_IDP = ''
    IData = ''
    PT_Code = ''
    Lifetime = ''

    Signature = uppercase(__md5(
                            __md5(Shop_IDP) + '&' + __md5(Order_IDP) + '&' +
                            __md5(Subtotal_P) + '&' + __md5(MeanType) + '&' +
                            __md5(EMoneyType) + '&' + __md5(Lifetime) + '&' +
                            __md5(Customer_IDP) + '&' + __md5(Card_IDP) + '&' +
                            __md5(IData) + '&' + __md5(PT_Code) + '&' +
                            __md5(_password)
                )
    )
    return Signature


def get_user(username):
    try:
        return Users108.objects.get(login=username, is_deleted=0)
    except User.DoesNotExist:
        return None


def is_promised_pay_possible(_account_id):
    days_30 = (time.time() - 2592000)
    return not PaymentTransactions.objects.filter(
        Q(account_id=_account_id) & ~Q(burn_time=0) &
        Q(burn_time__gte=days_30)
    ).exists()


class PromisedPay(View):
    def post(self, request):
        _login = request.session.get('user_login')

        if _login is None:
            return Http404

        balance = request.POST.get('balance')
        account_id = request.POST.get('account_id')

        cursor = connection.cursor()
        cursor.execute("SELECT UTM5_get_periodic_sum(%s);", (account_id,))
        periodic_sum = cursor.fetchone()[0]
        credit_sum = str(abs(int(balance)) + periodic_sum)

        if not balance or not account_id:
            return Http404

        if not is_promised_pay_possible(account_id):
            return Http404

        # balance = str(abs(int(balance)))
        account_id = request.POST.get('account_id')
        burn_time = str(int(time.time()) + 172800)  # 48hrs

        program_name = './ourfa_client'
        payment_args = [
            '-account_id', account_id,
            '-payment', credit_sum,
            '-burn_date', burn_time,
        ]

        command = [program_name]
        command.extend(ourfa_args)
        command.extend(payment_args)

        output = subprocess.Popen(
            command,
            stdout=subprocess.PIPE).communicate()[0]

        return HttpResponse(
            json.dumps({'balance': 0}),
            content_type="application/json"
        )

class PreparePaymentData(View):
    def post(self, request):
        _login = request.session.get('user_login')

        if _login is not None:
            _sum = request.POST.get('payment_sum')
            if _sum is None:
                return HttpResponse(
                    json.dumps({'sum': 'None'}),
                    content_type="application/json"
                )

            response_data = {}
            response_data['Shop_IDP'] = '00015227'
            response_data['Order_IDP'] = generate_order_idp(_login, _sum)
            response_data['CallbackFields'] = 'Customer_IDP BillNumber Total'
            response_data['Subtotal_P'] = _sum
            response_data['Customer_IDP'] = _login
            response_data['URL_RETURN_OK'] = 'http://lk.108telecom.ru/'
            response_data['URL_RETURN_NO'] = 'http://lk.108telecom.ru/'

            _signature = make_signature(response_data, os.environ.get('DJANGO_UNITELLER_PASSWORD'))
            response_data['Signature'] = _signature

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return Http404


class LoginFormView(View):
    def get(self, request):
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST.get('login')
        password = request.POST.get('password')
        try:
            user_to_auth = get_user(username)
        except Exception as e:
            user_to_auth = None

        if user_to_auth is not None and user_to_auth.password == password:
            request.session['user_login'] = user_to_auth.login
            return HttpResponseRedirect("/", context)
        else:
            context['login_error'] = 'Ошибка: логин или пароль введены неверно.'
            return render(request, 'login.html', context)


class Logout(View):
    def get(self, request):
        request.session.flush()
        if context.get('login_error'):
            del context['login_error']

        return HttpResponseRedirect('/')


class Main(View):
    def __init__(self):
        super().__init__()
        self.context = {}
        self.context['notices'] = []
        self.context['alerts'] = []

    def get_tariff_info(self, _account):
        try:
            tariff_link_obj = AccountTariffLink.objects.get(
                                    account_id=_account,
                                    is_deleted=0)
        except:
            self.context['tariff_name'] = 'Тариф не установлен'
            self.context['tariff_period'] = 'Расчетный период не установлен'
        else:
            tariff_obj = Tariffs.objects.get(id=tariff_link_obj.tariff_id,
                                             is_deleted=0)
            self.context['tariff_name'] = tariff_obj.name

            discount_periods_obj = DiscountPeriods.objects.get(pk=tariff_link_obj.discount_period_id)
            tariff_period = ' - '.join([datetime.utcfromtimestamp(
                                        discount_periods_obj.start_date).strftime('%d-%m-%Y'),
                                        datetime.utcfromtimestamp(
                                        discount_periods_obj.end_date).strftime('%d-%m-%Y'),
                                        ]
            )
            self.context['tariff_period'] = tariff_period

    def get_promised_pay_info(self, _account):
        try:
            if is_promised_pay_possible(_account) and self.context.get(
                    'balance') and self.context['balance'] < 0:
                self.context['promised_pay'] = 1
            else:
                self.context['promised_pay'] = 0
        except:
            self.context['promised_pay'] = 0

    def get(self, request):
        _user_login = request.session.get('user_login')

        if _user_login is None:
            return HttpResponseRedirect("accounts/login/")

        self.context['user_login'] = _user_login
        user_to_auth = get_user(_user_login)
        self.context['user_obj'] = user_to_auth

        account_obj = Accounts.objects.get(pk=user_to_auth.id, is_deleted=0)

        self.context['account_obj'] = account_obj
        self.context['balance'] = round(account_obj.balance-0.5)

        if account_obj.credit > 0:
            self.context['notices'].append(
                'Активирована услуга "обещанный платеж"! Вам необходимо '
                'пополнить баланс во избежание блокировки услуг.'.format(
                    int(account_obj.credit))
            )

        # self.context['alerts'].append('Скоро Новый Год!')

        user_account = user_to_auth.basic_account

        self.get_tariff_info(user_account)
        self.get_promised_pay_info(user_account)

        return render(request, 'lk_main.html', self.context)
