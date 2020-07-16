from django.db import models

# Create your models here.


class Jumbo(models.Model):
    titel = models.CharField(max_length=100)
    untertitel = models.CharField(max_length=250)
    inhalt = models.TextField()

    def __str__(self):
        return '{}'.format(self.titel)

class Impressum(models.Model):
    title = models.CharField(default="Impresssum", max_length=50, editable=False)
    content = models.TextField(default="Impressum fehlt!! kontaktieren sie bitte den Systemadministrator!!")
    def __str__(self):
        return '{}'.format(self.title)