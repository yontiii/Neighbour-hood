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
    
    business_form = BusinessForm(request.POST)
    if request.method == 'POST':
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = request.user
            business.location = location
            business.save()
        return redirect('single_hood',location)
    
    else:
        business_form = BusinessForm()
        
        
    
    
    return render(request,'hood.html',{"location":location,"businesses":businesses,'business_form':business_form})
