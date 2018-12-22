from django.shortcuts import render
from django.views import View

from .models import BusinessCategory, FinancialCategory, FinancialProfile, BusinessProfile
# Create your views here.

class getBCat(View):
    def get(self, request, slug):
        return render(request, 'businessprofile.html')

class getFCat(View):
    def get(self, request, slug):
        return render(request, 'businessprofile.html')