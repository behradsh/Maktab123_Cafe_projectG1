from django.db import models
from menu.models import MenuItems
from customer.models import Customers

STATUS_CHOICES = (
        ("waiting", "waiting"),
        ("cooking", "cooking"),
        ("served", "served"))
# Create your models here.
class Tables(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=50,blank=False,null=False)
    current_order = models.IntegerField()

class Orders(models.Model):
    table = models.ForeignKey(Tables,on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,blank=False,null=False,choices=STATUS_CHOICES,default="ongoing")
    timestamp = models.DateTimeField(auto_now_add=True)

class OrdersDetails(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(MenuItems,on_delete=models.DO_NOTHING)
    numbers = models.IntegerField()
    subtotal_price = models.DecimalField(max_digits=7,decimal_places=2)

class Receipts(models.Model):
    order = models.OneToOneField(Orders,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7,decimal_places=2)
    final_price = models.DecimalField(max_digits=7,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)