from django.urls import path 
from  .import views 



app_name = 'New_Arrival'

urlpatterns = [
    
    path('item_list', views.item_list, name= 'item_list' ),
    path ('Order_details', views.Order_details, name= 'order_details'),
    path ('newarrivals', views.newarrivals, name = 'newarrivals'), 
    path ('feedback', views.feedback, name = 'feedback')
]