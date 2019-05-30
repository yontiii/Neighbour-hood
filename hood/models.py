from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    
    
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    neighborhood = models.ForeignKey(Neighbourhood,null=True,blank=True) 
    
class Business(models.Model):
    
    


