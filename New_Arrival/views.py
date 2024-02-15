from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from .models import Item, Order, Feedback, NewArrivals, Customer
from .forms import SignupForm, LoginForm, NewItemForm

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

def signup (request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form = SignupForm()
    return render(request, 'signup.html',{'form':form})

def login (request):
    form = LoginForm()
    return render (request, 'login.html',{'form':form})


def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            NewArrivals = form.save(commit=False)
            NewArrivals.created_by = request.user
            NewArrivals.save()

            form.save()
            print ('you have sucessfully saved the new items')
            return redirect(request, 'new.html')
    else:
        form =NewItemForm()

    return render (request,'new.html', {'form':form ,'title':'New Item' } )
