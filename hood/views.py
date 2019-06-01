from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.http import Http404
from .forms import *
 

# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request,'index.html',{"hoods":hoods})

def single_hood(request,location):
 
    location = Neighbourhood.objects.get(name=location) 
    print(location.id)
    businesses = Business.get_location_businesses(location.id)
    
    business_form = 
               
    
    return render(request,'hood.html',{"location":location,"businesses":businesses})
