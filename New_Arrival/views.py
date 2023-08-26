from django.shortcuts import render
from .models import Item, Order_details, Feedback, NewArrivals 
# Create your views here.

def home (request): 
    return render (request, 'home.html')

def base (request):
    return render (request, 'base.html')

def item_list(request): 
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "item_list.html", context )


def Order_details(request):
    context = { 
        "order_details" : Order_details.objects.all()
    }

    return render (request, "order_details.html", context)
def feedback(request):
    context = { 
        feedback : Feedback.objects.all()
    }
    return render (request, "feedback.html", context)


def newarrivals(request):
    context = {
        newarrivals : NewArrivals.objects.all()
    }
    return render( request, "newarrivals.html", context )


