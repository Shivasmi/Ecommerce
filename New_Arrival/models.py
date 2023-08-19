from django.conf import settings 
from django.db import models 
from django.contrib.auth.models import User 

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return self.title

class OrderItem(models.Model): 
    item = models.ForeignKey(Item,on_delete= models.CASCADE)

    def __str__(self):
        return self.title 
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self): 
        return self.user.username 
    
class Customer (models.Model): 
    user=models.OneToOneField(User, on_delete= models.CASCADE)
    address = models.CharField(max_length= 50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=30) 
    
    @property
    def get_name(self):
        return self.user.first_name+ " "+self.user.last_name

    def __str__(self):
        return self.user.first_name
    
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    feedback= models.CharField(max_length=300)
    date= models.DateField(auto_now_add=True, blank= True)

    def __str__(self):
        return self.name
    
class NewArrivals(models.Model):
    brand = models.CharField(max_length=50)
    categories = models.ManyToManyField(to= 'NewArrivals')
    descriptions = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_new_arrival = models.BooleanField(default= False)
    image = models.ImageField(upload_to= 'newarrival_images/')

    def __str__(self):
        return self.brand
    
class Order_details(models.Model):
    order = models.CharField(max_length=100)
    num_of_item = models.IntegerField()
    total_summary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order
    
    
    