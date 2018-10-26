from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Users108
import time
from hashlib import md5 as hashlib_md5
import json
import os
import requests


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
        return Users108.objects.get(login=username)
    except User.DoesNotExist:
        return None


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
            response_data['Shop_IDP'] = '00015162'
            response_data['Order_IDP'] = generate_order_idp(_login, _sum)
            response_data['CallbackFields'] = 'Customer_IDP BillNumber Total'
            response_data['Subtotal_P'] = _sum
            response_data['Customer_IDP'] = _login
            response_data['URL_RETURN_OK'] = 'http://lk.108telecom.ru/'
            response_data['URL_RETURN_NO'] = 'http://lk.108telecom.ru/'

            # os.environ.get('UNITELLER_PASSWORD')
            _signature = make_signature(response_data, os.environ.get('DJANGO_UNITELLER_PASSWORD'))
            response_data['Signature'] = _signature

            # r = requests.post("https://wpay.uniteller.ru/pay/", data=response_data)

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
            # return HttpResponse(
            #     r.text,
            #     content_type="text/html"
            # )
        else:
            return Http404


class LoginFormView(View):
    def get(self, request):
        return render(request, 'login_form.html', context)

    def post(self, request):
        username = request.POST.get('login')
        password = request.POST.get('password')
        try:
            user_to_auth = get_user(username)
        except:
            user_to_auth = None

        if user_to_auth is not None and user_to_auth.password == password:
            request.session['user_login'] = user_to_auth.login
            return HttpResponseRedirect("/")
        else:
            context['login_error'] = 'Ошибка: логин или пароль введены неверно.'
            return render(request, 'login_form.html', context)


class Logout(View):
    def get(self, request):
        request.session.flush()
        if context.get('login_error'):
            del context['login_error']

        return HttpResponseRedirect('/')


class Main(View):
    def get(self, request):
        _user_login = request.session.get('user_login')
        if _user_login is not None:
            context['page'] = '108'
            context['sess'] = {}
            context['user_login'] = _user_login
            for name, value in request.session.items():
                context['sess'][name] = value

            return render(request, 'index.html', context)
        else:
            return HttpResponseRedirect("accounts/login/")
