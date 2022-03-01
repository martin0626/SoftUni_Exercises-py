from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from petstagramFinal.accounts.forms import LoginForm, RegisterForm, ProfileForm
from petstagramFinal.accounts.models import UserProfile
from petstagramFinal.pets.models import Pet


def profile_view(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile view', pk)

    pets = Pet.objects.filter(user_id=profile.user.id)
    form = ProfileForm()
    context = {
        'pets': pets,
        'profile': profile,
        'form': form,
    }

    return render(request, 'accounts/user_profile.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pets list')
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('landing page')

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


def sign_out(request):
    logout(request)
    return redirect('landing page')
