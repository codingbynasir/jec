from django.shortcuts import render
from django.views import View
from .models import Company
# Create your views here.

class getHome(View):
    def get(self, request):
        content=Company.objects.all()
        context={"content":content}
        return render(request,'Home.html',context)