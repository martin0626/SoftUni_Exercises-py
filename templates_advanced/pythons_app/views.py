from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .emails import send_email_message
from .forms import PythonCreateForm, LoginForm, ProfileForm, UserCreationForm
from .models import Python, Profile


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    ordering = ('name', )


class CreatePython(CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index')


class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            send_email = send_email_message(email, username)
            form.save()
        return redirect('login')
    else:
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'register.html', context)


@login_required
def profile(request):
    profile_f = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_f)
        if form.is_valid():
            form.save()
            return redirect('index')
        return redirect('create')
    else:
        context = {
            'form': ProfileForm(instance=request.user)
        }
        return render(request, 'profile.html', context)
