from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class GalleryContent(models.Model):
    title=models.CharField(max_length=200)
    sutitle=models.CharField(max_length=200,null=True, blank=True)
    image=models.ImageField(null=True, blank=True, help_text="Don't upload image, if it is not image gallery category")
    video=models.URLField(null=True, blank=True, help_text="link from youtube or vimeo. Don't upload image, if it is not image gallery category")
    pdf=models.FileField(null=True, blank=True, help_text="only for seminar gallery")

    def get(self):
        return self.title