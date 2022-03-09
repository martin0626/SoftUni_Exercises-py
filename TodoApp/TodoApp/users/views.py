from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from TodoApp.users.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my todos')

    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'User/register_view.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('my todos')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'User/login_view.html', context)


def logout_view(request):
    logout(request)
    return redirect('my todos')
