from django.urls import path
from petstagramFinal.pets.views import pets, pets_details, like_pet, create_pet, edit_pet, del_photo, make_comment

urlpatterns = [
    path('pets/', pets, name='pets list'),
    path('details/<int:pk>', pets_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('pets/create/', create_pet, name='create'),
    path('pets/edit/<int:pk>', edit_pet, name='edit'),
    path('pets/delete/<int:pk>', del_photo, name='delete'),
    path('pets/comment/<int:pk>', make_comment, name='comment'),

]

