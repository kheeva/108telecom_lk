from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


context = {}


class LoginFormView(View):
    def get(self, request):
        context = {}
        return render(request, 'login_form.html', context)


def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            context['login_error'] = 'Ошибка: логин или пароль введены неверно.'
            context['username'] = username
            return render(request, 'login_form.html', context)
    raise Http404


@login_required
def main(request):
    context['page'] = '108'
    return render(request, 'index.html', context)
