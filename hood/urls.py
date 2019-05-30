from django.conf import url
from .import views

urlpatterns = [
    url('^$',views.index,name='index'),
    
]