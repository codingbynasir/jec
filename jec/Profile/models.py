from django.db import models

# Create your models here.
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class FinancialCategory(models.Model):
    name=models.CharField(max_length=100)
    description=RichTextUploadingField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FinancialCategory, self).save(*args, **kwargs)

class FinancialProfile(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    image=models.ImageField()
    file=models.FileField()
    category=models.ForeignKey(FinancialCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FinancialProfile, self).save(*args, **kwargs)


class BusinessCategory(models.Model):
    name=models.CharField(max_length=100)
    description = RichTextUploadingField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BusinessCategory, self).save(*args, **kwargs)


class BusinessProfile(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    description=RichTextUploadingField()
    image = models.ImageField()
    video=models.URLField()
    category = models.ForeignKey(FinancialCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BusinessProfile, self).save(*args, **kwargs)
