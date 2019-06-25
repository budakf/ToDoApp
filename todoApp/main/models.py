from django.db import models
from datetime import datetime
# from tinymce.widgets import TinyMCE


# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=250)
    detail = models.TextField()
    publisher = models.CharField(max_length=80, default="budakf")
    published_time = models.DateTimeField(default=datetime.now)
    isAchieved = models.BooleanField(default=False)

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()},
    # }

    def __str__(self):
        return self.name

    def create(self, name, detail, publisher):
        self.name = name
        self.detail = detail
        self.publisher = publisher
        self.save()
    
    class Meta:
        verbose_name_plural = u"Notes"
        verbose_name = u"Note"
