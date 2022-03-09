from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from TodoApp.users.models import TodoUser


class BootsTrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class RegisterForm(BootsTrapMixin, UserCreationForm):
    class Meta:
        model = TodoUser
        fields = ['username', 'email']

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )


class LoginForm(BootsTrapMixin, AuthenticationForm):
    pass
