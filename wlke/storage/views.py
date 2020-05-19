from django.shortcuts import render

from .models import Datei

# Create your views here.


def index(request):
    dateien = Datei.objects.all().order_by("name")
    return render(request, 'storage/storage_index.html')
