from django.shortcuts import render,HttpResponse, get_object_or_404, Http404, redirect
from django.views import View
from io import BytesIO
from .models import Company, Shareholder, RulesCategory, RulesRegulation, Rank, Message
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .global_content import r, gallery_category, f_category, b_category
from django.template.loader import get_template
from xhtml2pdf import pisa
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
            content = Shareholder.objects.get(rank__name__icontains="founder")
            message=get_object_or_404(Message, shareholder__id=content.id)
            context={
                "content": content,
                "message":message,
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
            content = Shareholder.objects.exclude(rank__name__startswith="advisory")
            context={
                "shareholders": content,
                "cat":r,
                "gallery_cat":gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)

        elif rank == "governing":

            tst = Shareholder.objects.exclude(rank__name__startswith="advisory")
            context = {
                "shareholders": tst,
                "cat": r,
                "gallery_cat": gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)

        elif rank == "advisory":
            content = Shareholder.objects.filter(rank__name__startswith="advisory")
            context = {
                "shareholders": content,
                "cat": r,
                "gallery_cat": gallery_category,
                "f_cat": f_category,
                "b_cat": b_category
            }
            return render(request, "shareholder.html", context)

        elif rank == "co-governing":
            content = Shareholder.objects.filter(rank__name__startswith="ordinary")
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

def render_pdf(template, data={}):
    t=get_template(template)
    bind=t.render(data)
    byte=BytesIO()
    pdf = pisa.pisaDocument(BytesIO(bind.encode("ISO-8859-1")), byte)
    if pdf.err:
        return None
    else:
        return HttpResponse(byte.getvalue(),content_type="application/pdf")



class viewPDF(View):
    def get(self, request, slug):
        try:
            data=get_object_or_404(RulesRegulation, slug=slug)
        except:
            return Http404("Object is not found")

        pdf = render_pdf("pdf.html", {"data":data})
        return HttpResponse(pdf, content_type="application/pdf")