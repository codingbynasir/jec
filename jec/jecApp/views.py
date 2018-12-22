from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views import View
from .models import Company, Shareholder, RulesCategory, RulesRegulation
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .global_content import r, gallery_category, f_category, b_category
# Create your views here.

class getHome(View):
    def get(self, request):
        content=Company.objects.all()

        context={
            "content":content,
            "cat":r,
            "gallery_cat":gallery_category,
            "f_cat":f_category,
            "b_cat":b_category
        }
        return render(request,'Home.html',context)

class getFounder(View):
    def get(self, request):
        try:
            content = get_object_or_404(Shareholder, rank="founder")
            context={
                "content": content,
                "cat": r,
                "gallery_cat": gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "founder.html", context)
        except:
            raise Http404("Sorry! No content found")

class getShareholder(View):
    def get(self, request, rank):
        #content = Shareholder.objects.all()
        if rank == "ordinary":
            content = Shareholder.objects.exclude(rank="advisory")
            context={
                "shareholders": content,
                "cat":r,
                "gallery_cat":gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)

        elif rank == "governing":
            content = Shareholder.objects.exclude(designation=None, rank="advisory")
            context = {
                "shareholders": content,
                "cat": r,
                "gallery_cat": gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)

        elif rank == "advisory":
            content = Shareholder.objects.filter(rank="advisory")
            context = {
                "shareholders": content,
                "cat": r,
                "gallery_cat": gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)

        elif rank == "co-governing":
            content = Shareholder.objects.filter(rank="ordinary", designation=None)
            context = {
                "shareholders": content,
                "cat": r,
                "gallery_cat": gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)
        else:
            raise Http404

'''----------------------------
---Login to your account-------
-------------------------------'''
class getLogin(View):
    def get(self, request):
        context={
            "cat":r,
            "gallery_cat":gallery_category,
            "f_cat": f_category,
            "b_cat": b_category
        }
        return render(request, 'login.html',context)
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        auth=authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('index')
        else:
            messages.error(request, 'Username or password is error')
            return redirect('login')


class lawRules(View):
    def get(self, request, slug):
        try:
            cat=get_object_or_404(RulesCategory,slug=slug)
        except:
            return Http404("No content found with this query")

        acts=RulesRegulation.objects.filter(category__slug=slug)
        context={
            "act_cat":cat,
            "acts":acts,
            "cat":r,
            "gallery_cat":gallery_category,
            "f_cat": f_category,
            "b_cat": b_category
        }
        return render(request,'rules_regulation.html', context)