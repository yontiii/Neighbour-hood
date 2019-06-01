from django import forms
from .models import *

class BusinessForm(models.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']
        
class PostsForm(models.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']
        
class 
    