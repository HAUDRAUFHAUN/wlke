from django.shortcuts import render

# Create your views here.


def index(request):

    if request.method == 'POST':
        print(request)
    return render(request, 'notes/notes_index.html')
