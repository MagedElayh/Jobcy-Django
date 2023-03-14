from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'