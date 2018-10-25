from django.conf.urls import url
from django.urls import path

from authapp.views import login, LoginFormView, main


urlpatterns = [
    url(r'^accounts/login/$', LoginFormView.as_view(), name='login_form'),
    url(r'^login/$', login, name='login'),
    url(r'^$', main, name='main'),
]
