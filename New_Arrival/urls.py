from django.contrib import admin
from django.urls import path, reverse
from . import views 


app_name = 'New_Arrival'

urlpatterns = [
    path ('', views.home, name ='home'),
    path ('home', views.home, name='home'),
    path ('item_list', views.item_list, name='item_list' ),
    path ('order_details', views.order_details, name='order_details'),
    path ('newarrivals', views.newarrivals, name ='newarrivals'), 
    path ('feedback', views.feedback, name ='feedback'),
    path ('customer', views.customer, name ='customer'),
    path ('signup/', views.signup, name ='signup'),
    path ('login/', views.login, name ='login'),
    path ('new/', views.new, name ='new'),
 
]


