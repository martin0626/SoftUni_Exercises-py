from django.contrib import admin

from RESTFrameworkDemo.api.models import Likes


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('like',)
