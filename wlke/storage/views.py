from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Datei

# Create your views here.


def index(request):
    dateien = Datei.objects.all().order_by("name")
    frontend_data = {'dateien': dateien, }
    return render(request, 'storage/storage_index.html', frontend_data)
