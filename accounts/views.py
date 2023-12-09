from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm, LoginForm


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


def user_logout(request):
    logout(request)
    return redirect('login')
