from django.shortcuts import render
from .models import Item, Order_details, Feedback, NewArrivals 
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


