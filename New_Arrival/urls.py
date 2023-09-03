from django.contrib import admin
from django.urls import path 
from . import views 



app_name = 'New_Arrival'

urlpatterns = [
    path ('', views.home, name = 'home'),
    path ('home', views.home, name= 'home'),
    path ('item_list', views.item_list, name = 'item' ),
    path ('order_details', views.Order_details, name= 'order_details'),
    path ('newarrivals', views.newarrivals, name = 'newarrivals'), 
    path ('feedback', views.feedback, name = 'feedback'),
]

