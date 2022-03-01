from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='snakes')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    birth_date = models.DateField(null=True, blank=True)

