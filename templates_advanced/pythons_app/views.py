from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PythonCreateForm, LoginForm, ProfileForm
from .models import Python, Profile


# Create your views here.
# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons})


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'


class CreatePython(CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index')


# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#         return render(req, 'create.html', {'form': form})
#     else:
#         data = req.POST
#         form = PythonCreateForm(data, req.FILES)
#         if form.is_valid():
#             python = form.save()
#             python.save()
#             return redirect('index')


# def login_user(request):
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'])
#             if user:
#                 login(request, user)
#             return redirect('index')
#     else:
#         context = {
#             'form': LoginForm()
#         }
#         return render(request, 'login.html', context)


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
            form.save()
        return redirect('login')
    else:
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'register.html', context)


class RegisterView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('index')


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
