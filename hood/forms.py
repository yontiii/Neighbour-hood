from django import forms
from .models import *

class BusinessForm(models.ModelForm):
    class Meta:
        model = Business
        fields = ('')