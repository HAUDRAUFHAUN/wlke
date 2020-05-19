from django.shortcuts import render

from .models import Datei

# Create your views here.


def index(request):
    return render(request, 'storage/storage_index.html')
