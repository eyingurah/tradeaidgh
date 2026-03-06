from django import forms

from .models import ContactForm


class CForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ("name", "email", "subject", "message")
