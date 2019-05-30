from django.db import models


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
    hood_update = cls.objects.filter(name)

    
    
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    neighborhood = models.ForeignKey(Neighbourhood,null=True,blank=True) 
    
class Business(models.Model):
    business_name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    business_email = models.EmailField(max_length=200)
    business_hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE) 
 
    
    


