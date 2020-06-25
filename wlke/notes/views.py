from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Notiz

from django.contrib.auth.models import User

# Create your views here.


def index(request):

    if request.method == 'POST':
        notetitle = request.POST.get('note-title')
        notebody = request.POST.get('note-body')
        # print(notetitle + '  ' + notebody)
        user = request.user
        note = Notiz(
            benutzer=user, titel=notetitle, body=notebody)
        note.save()
        # print(note)
    return render(request, 'notes/notes_index.html')


def edit(request, note_id):
    return HttpResponse(request, "Hier werden Notizen bearbeitet...")


def view(request, note_id):
    return HttpResponse(request, "Notiz anschauen")


def delete(request, note_id):
    note = Notiz.objects.all().filter(id=note_id)
    note.delete()

    return HttpResponseRedirect("/notes/")
