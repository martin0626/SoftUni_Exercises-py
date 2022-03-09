from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from TodoApp.users.managers import TodoUserManager


class TodoUser(AbstractUser, PermissionsMixin):
    USERNAME_MAX_LEN = 25
    EMAIL_MAX_LEN = 30
    USERNAME_MIN_LEN = 3

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
        validators=[MinLengthValidator(USERNAME_MIN_LEN)],
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        unique=True,
        validators=[MinLengthValidator(USERNAME_MIN_LEN)],
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    objects = TodoUserManager()
