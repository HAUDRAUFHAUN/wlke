from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .models import Datei


def index(request):
    if request.method == 'POST' and request.FILES['file']:
        print(request.FILES)
        file = request.FILES['file']
        new_datei = Datei(benutzer=request.user, datei=file, name=file.name)
        new_datei.save()
        return HttpResponseRedirect('/storage/')
    return render(request, 'storage/storage_index.html',)
