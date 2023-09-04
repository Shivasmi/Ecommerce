from django.shortcuts import render
from .models import Item, Order, Feedback, NewArrivals, Customer
# Create your views here.

def home(request):
    return render (request, 'home.html')

def item_list(request): 
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "item_list.html", context )


def order_details(request):
    summary = Order.objects.all()
    context = { 
        "order_details" : summary
    }

    return render (request, "order_details.html", context)
def feedback(request):
    context = { 
        'feedback' : Feedback.objects.all()
    }
    return render (request, "feedback.html", context)

def customer(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers
    }
    return render (request, "customer.html", context)

def newarrivals(request):
    context = {
        'newarrivals' : NewArrivals.objects.all()
    }
    return render( request, "newarrivals.html", context )


