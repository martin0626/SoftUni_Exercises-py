from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from TodoApp.users.forms import RegisterForm, LoginForm


class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'User/register_view.html'
    success_url = reverse_lazy('my todos')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'User/login_view.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('my todos')


class UserLogoutView(LogoutView):
    pass



