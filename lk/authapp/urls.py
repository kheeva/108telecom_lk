from django.conf.urls import url
from django.urls import path

from authapp.views import LoginFormView


urlpatterns = [
    url(r'^$', LoginFormView.as_view(), name='login_form'),
]