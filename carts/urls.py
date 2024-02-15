from django.urls import path 

from . import views

urlpatterns = [
    path ('', views.carts_summary, name = 'carts_summary'),
    path ('add/', views.carts_add, name = 'carts_add'),
    path ('delete', views.carts_delete, name = 'carts_delete'),
    path ('update', views.carts_update, name = 'carts_update'),


]
