from django.shortcuts import render
from .models import Item, Order_details
# Create your views here.

def item_list(request): 
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "item_list.html", context )


def Order_details(request):
    context = { 
        Order_details: Order_details.objects.all()
    }

    return render (request, "order_details.html", context)
