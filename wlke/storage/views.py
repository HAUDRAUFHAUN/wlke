from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Datei

# Create your views here.


def index(request):
    neue_datei = request.POST.get('datei')
    print(neue_datei)
    dateien = Datei.objects.all().order_by("name")
    frontend_data = {'dateien': dateien, }
    return render(request, 'storage/storage_index.html', frontend_data)
