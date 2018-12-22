from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.contrib import messages
from jecApp.global_content import r, gallery_category,f_category,b_category
# Create your views here.
class Contact(View):
    def get(self, request):
        context={
            "form":ContactForm,
            "cat":r,
            "gallery_cat":gallery_category,
            "f_cat":f_category,
            "b_cat":b_category
        }
        return render(request, 'contact.html', context)
    def post(self, request):
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact form is saved successfully')
            return redirect('contact')
        else:
            messages.error(request, 'Sorry! Contact form is not submitted!')
            return redirect('contact')