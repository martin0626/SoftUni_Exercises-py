from django.urls import path

from TodoApp.users.views import UserLoginView, UserRegistrationView, UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register view'),
    path('login/', UserLoginView.as_view(), name='login view'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]