from django import forms
from .models import Note
from datetime import datetime


class NoteForm(forms.ModelForm):
    name = forms.CharField(max_length=250) 
    detail = forms.Textarea()

    class Meta:
        model = Note
        fields = ["name", "detail",]


