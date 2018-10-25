from django.conf.urls import url
from django.urls import path

from authapp.views import Logout, LoginFormView, Main, PreparePaymentData


urlpatterns = [
    url(r'^accounts/login/$', LoginFormView.as_view(), name='login_form'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^$', Main.as_view(), name='main'),
    url(r'^pay_prepare/$', PreparePaymentData.as_view(), name='pay_prepare'),
]
