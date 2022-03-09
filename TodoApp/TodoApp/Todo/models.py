from django.db import models

from TodoApp.users.models import TodoUser


class Todo(models.Model):
    TITLE_MAX_LEN = 25
    DESCRIPTION_MAX_LEN = 200

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
    )

    is_done = models.BooleanField(
        default=False,
    )

    owner = models.ForeignKey(
        TodoUser,
        on_delete=models.CASCADE,
    )
