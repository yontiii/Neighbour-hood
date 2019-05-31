from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.http import Http404
 

# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request,'index.html',{"hoods":hoods})

def single_hood(request,hood_id):
    try:
       hoods = Neighbourhood.objects.get(id=hood_id) 
       businesses = Business.get_location_businesses()
    except Exception as e:
        raise Http404()               
    
    return render(request,'hood.html',{"hoods":hoods,"businesses":businesses})
