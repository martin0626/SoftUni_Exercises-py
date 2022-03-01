from django.urls import path
from petstagramFinal.accounts.signals import *
from petstagramFinal.accounts.views import profile_view, sign_up, sign_in, sign_out

urlpatterns = [
    path('profile/<int:pk>', profile_view, name='profile view'),
    path('signup/', sign_up, name='sign up'),
    path('signin/', sign_in, name='sign in'),
    path('signout/', sign_out, name='sign out'),
]