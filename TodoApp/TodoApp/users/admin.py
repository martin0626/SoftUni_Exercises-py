from django.contrib import admin

from TodoApp.Todo.models import Todo


@admin.register(Todo)
class AdminTodoUser(admin.ModelAdmin):
    list_display = ['title']
