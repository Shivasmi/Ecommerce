from django.contrib import admin
from django.urls import path 
from New_Arrival import views



app_name = 'New_Arrival'

urlpatterns = [
    path ('base', views.base, name = 'base' ),
    path ('item_list', views.item_list, name = 'item_list' ),
    path ('home', views.home, name= 'home'),
    path ('order_details', views.Order_details, name= 'order_details'),
    path ('newarrivals', views.newarrivals, name = 'newarrivals'), 
    path ('feedback', views.feedback, name = 'feedback'),
]

