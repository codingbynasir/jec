from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.utils.text import slugify


class Company(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=150)
    content=RichTextUploadingField()
    image=models.ImageField()

    def __str__(self):
        return self.title


class Designation(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name.title()

class Rank(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name.title()



class Shareholder(models.Model):
    name=models.CharField(max_length=100)
    designation = models.ManyToManyField(Designation)
    rank = models.ManyToManyField(Rank)
    image= models.ImageField()
    education=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    def design(self):
        return self.designation.name

class Message(models.Model):
    shareholder=models.ForeignKey(Shareholder, on_delete=models.CASCADE)
    banner=models.ImageField()
    message_text=RichTextUploadingField(null=True, blank=True)
    def __str__(self):
        return self.shareholder.name.title()

class RulesCategory(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200, null=True, blank=True)
    category_details=RichTextUploadingField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(RulesCategory, self).save(*args, **kwargs)


class RulesRegulation(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200, null=True, blank=True)
    category=models.ForeignKey(RulesCategory, on_delete=models.CASCADE)
    description=RichTextUploadingField()
    posted_on=models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image=models.ImageField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(RulesRegulation, self).save(*args, **kwargs)