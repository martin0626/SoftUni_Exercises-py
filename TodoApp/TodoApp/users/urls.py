from django.urls import path

from TodoApp.users.views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register view'),
    path('login/', login_view, name='login view'),
    path('logout/', logout_view, name='logout'),
]