from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class LoginFormView(View):
    def get(self, request):
        context = {}
        return render(request, 'login_form.html', context)
