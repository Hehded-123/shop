from django import forms
from django.contrib.auth.models import User

class ContactUsForm(forms.Form):
    class Meta:
        model = ContactUs
        fields = ['name', 'email','phone', 'message']