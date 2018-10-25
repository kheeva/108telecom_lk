from django.contrib.auth.models import User
from django import forms
from .models import Users108


class MyPortalBackend(object):
    def authenticate(self, **kwargs):
        try:
            username = kwargs['username']
            password = kwargs['password']

            user_to_auth = self.get_user(username)

            if user_to_auth is None and user_to_auth.password != password:
                raise forms.ValidationError(
                    _("username or password mismatch")
                )
        except KeyError:
            raise forms.ValidationError(
                _("Programming Error")
            )
        else:
            return user_to_auth


    def get_user(self, username):
        try:
            return Users108.objects.get(login=username)
        except User.DoesNotExist:
            return None
