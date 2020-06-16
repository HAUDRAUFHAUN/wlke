from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Notiz(models.Model):
    benutzer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notiz", null=False)
    titel = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Notizeb'
