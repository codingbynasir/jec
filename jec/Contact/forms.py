from django.contrib.admin.forms import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
