from django.contrib import admin
from .models import Note
from django.db import models
# from tinymce.widgets import TinyMCE


# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ["name","publisher","published_time", "isAchieved"]

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()},
    # }



admin.site.register(Note, NoteAdmin)