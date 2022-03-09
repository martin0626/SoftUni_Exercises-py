from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from TodoApp.users.models import TodoUser


@admin.register(TodoUser)
class AdminTodoUser(UserAdmin):
    list_display = ("username", "email", "is_staff")

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    search_fields = ("username", "email")

    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info",), {"fields": ("email",)}),
        (
            ("Permissions",),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),
            },
        ),
        (("Important dates",), {"fields": ("last_login", "date_joined")}),
    )
