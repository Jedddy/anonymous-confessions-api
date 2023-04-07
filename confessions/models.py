from django.db import models


class Confession(models.Model):
    title = models.CharField(max_length=40)
    confession = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.confession
