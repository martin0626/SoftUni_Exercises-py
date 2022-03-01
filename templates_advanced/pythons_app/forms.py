from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Python, Profile
from django import forms


class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        fields = '__all__'


class LoginForm(AuthenticationForm):
    user = None

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile()
        exclude = ['user']
