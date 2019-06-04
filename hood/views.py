from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.http import Http404
from .forms import BusinessForm,PostsForm
 

# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request,'index.html',{"hoods":hoods})

def single_hood(request,location):
 
    location = Neighbourhood.objects.get(name=location) 
    print(location.location)
    businesses = Business.get_location_businesses(location.id) 
    posts = Posts.get_location_posts(location.id)
    
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
        
    
    posts_form = PostsForm(request.POST)
    if request.method == 'POST':
        if posts_form.is_valid():
            posts = posts_form.save(commit=False)
            posts.user = request.user
            posts.location = location
            posts.save()
        return redirect('single_hood',location)
    
    else:
        posts_form = PostsForm()  
        
    context = {"location":location,
               "businesses":businesses,
               'business_form':business_form,
               "posts_form":posts_form,
                "posts":posts,
                }
    
    
    return render(request,'hood.html',context)
