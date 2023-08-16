from django.urls import path 
from .views import item_list
from .import views 


app_name = 'New_Arrival'

urlpatterns = [
    
    path('item_list', views.item_list, name= 'item_list' )
]