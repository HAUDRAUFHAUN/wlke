from django.db import models

# Create your models here.
class Datei(models.Model):
    datei = models.FileField()
    name = models.CharField(max_length=200)