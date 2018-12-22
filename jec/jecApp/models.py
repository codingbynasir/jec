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




class Shareholder(models.Model):
    name=models.CharField(max_length=100)
    message=RichTextUploadingField(null=True, blank=True)
    designation=models.CharField(null=True,blank=True,max_length=100, choices=(("chairman","Chairman"),("vice-chairman","Vice Chairman"),("general-secretary","General Secretary"),("board-member-1","Board Member 1"),("board-member-2","Board Member 2"),("board-member-3","Board Member 3")))
    rank=models.CharField(max_length=100, choices=(("founder","Founder"),("ordinary","Ordinary"),("governing","Governing"),("co-governing","Co-Governing"),("advisory","Advisory")))
    image= models.ImageField()
    education=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

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