from django.shortcuts import render
from django.views import View

from .models import Category, GalleryContent
# Create your views here.
class getCategory(View):
    def get(self, request, slug):
        return render(request, 'video-galler.html')