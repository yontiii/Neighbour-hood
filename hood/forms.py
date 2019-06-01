from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']
        
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']
        

    