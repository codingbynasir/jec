from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Company(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=150)
    content=RichTextUploadingField()
    image=models.ImageField()

    def __str__(self):
        return self.title

