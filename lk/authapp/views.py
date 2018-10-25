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
from django.conf import settings
import json


context = {}


def __md5(_str):
    return hashlib_md5(_str.encode()).hexdigest()


def generate_order_idp(login, sum):
    _time = str(int(time.time()))
    return __md5(''.join([login, sum, _time]))


def uppercase(_str):
    return _str.upper()


def make_signature(post_attrs, _password):
    _str = ''.join([
        post_attrs['Order_ID'],
        post_attrs['Status'],
        post_attrs['Customer_IDP'],
        post_attrs['BillNumber'],
        _password,
    ])
    return uppercase(__md5(_str))


def get_user(username):
    try:
        return Users108.objects.get(login=username)
    except User.DoesNotExist:
        return None


class PreparePaymentData(View):
    def post(self, request):
        _sum = request.POST.get('sum')
        if _sum is None:
            return HttpResponse(
                json.dumps({'sum': 'None'}),
                content_type="application/json"
            )

        _login = request.session['user_login']
        response_data = {}
        response_data['Shop_IDP'] = '00015162'
        response_data['Order_IDP'] = generate_order_idp(_login, _sum)
        response_data['CallbackFields'] = 'Customer_IDP BillNumber Total'
        response_data['Subtotal_P'] = _sum
        response_data['Customer_IDP'] = _login
        response_data['URL_RETURN_OK'] = 'http://lk.108telecom.ru/'
        response_data['URL_RETURN_NO'] = 'http://lk.108telecom.ru/'
        response_data['Submit'] = 'Оплатить'


        _signature = make_signature(response_data, settings.Base.ALLOWED_HOSTS)
        response_data['Signature'] = _signature

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


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
