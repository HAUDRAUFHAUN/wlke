from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Datei(models.Model):
    benutzer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="datei", null=True)
    datei = models.FileField(
        upload_to='data/adjkncvir1495kgsiqiy/', null=True, blank=True,)
    name = models.CharField(max_length=200)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dateien'
