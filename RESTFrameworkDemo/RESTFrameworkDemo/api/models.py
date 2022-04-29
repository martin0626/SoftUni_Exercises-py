from django.db import models


class Likes(models.Model):
    like = models.IntegerField(
        default=1,
    )
