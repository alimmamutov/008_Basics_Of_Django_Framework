from django import forms
from .models import *


class ClientProductOffer(forms.Form):
    category = forms.ModelChoiceField(label='Category', queryset=ProductCategory.objects.all())
    name = forms.CharField(max_length=128)
    short_desc = forms.CharField(max_length=60)
