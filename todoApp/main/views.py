from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .noteForm import NoteForm

# Create your views here.


def homePage(request):
    notes = Note.objects.all()
    form = NoteForm
    return render(request=request, template_name="main/home.html", context={"notes": notes, "form": form} )


def takeNote(request):
    if request.method == "POST":
        noteForm = NoteForm(request.POST)
        noteForm.publisher="budakf"
        if noteForm.is_valid:
            noteForm.save()
    
    return redirect("/")

def deleteNote(request):
    if request.method == "POST":
        form = request.POST
        noteName= form.get("note_name")
        noteDetail= form.get("note_detail")
        Note.objects.filter(name=noteName).filter(detail=noteDetail)[0].delete()
    
    return redirect("/")


def achieved(request):
    if request.method == "POST":
        form = request.POST
        noteName= form.get("note_name")
        noteDetail= form.get("note_detail")
        note = Note.objects.filter(name=noteName).filter(detail=noteDetail)[0]
        note.isAchieved = not note.isAchieved
        note.save()
        print(note.isAchieved)
    return redirect("/")
    
     