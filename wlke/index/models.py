from django.db import models

# Create your models here.


class Jumbo(models.Model):
    titel = models.CharField(max_length=100)
    untertitel = models.CharField(max_length=250)
    inhalt = models.TextField()
