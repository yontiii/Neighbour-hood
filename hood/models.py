from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    count = models.IntegerField(default=0)  
    
    def create_neighbourhood(self):
        self.save()
      
    def delete_neighbourhood(self):
        self.delete()
        
    @classmethod
    def find_by_id(cls,id):
        hoods = cls.objects.filter(id=id)
        return hoods  
    
    @classmethod
    def update_neighbourhood(cls)
    hood_update = cls.objects.filter(id=1).update(name='name')
    return hood_update

    def __str__(self):
        return self.name

    
    
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    neighborhood = models.ForeignKey(Neighbourhood,null=True) 
    
    def __str__(self):
        return self.title
    
class Business(models.Model):
    business_name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    business_email = models.EmailField(max_length=200)
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE) 
    
    
    def __str__(self):
        return self.title
    
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
 
    
    


