from django.shortcuts import render, HttpResponse
from .models import Notiz

from django.contrib.auth.models import User

# Create your views here.


def index(request):

    if request.method == 'POST':
        notetitle = request.POST.get('note-title')
        notebody = request.POST.get('note-body')
        # print(notetitle + '  ' + notebody)
        note = Notiz(
            titel=notetitle, body=notebody)
        note.save()
        # print(note)
    return render(request, 'notes/notes_index.html')


def edit(request):
    return HttpResponse(request, "Hier werden Notizen bearbeitet...")


def view(request):
    return HttpResponse(request, "Notiz anschauen")
