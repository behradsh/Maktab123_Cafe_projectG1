from django.db import models
from ..menu.models import MenuItems
from ..customer import Customers

STATUS_CHOICES = (("ongoing","ongoing"),
                  ("notpaid","notpaid"),
                  ("ordered","ordered"),
                  ("failed","failed"),)
# Create your models here.
class tables(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=50,blank=False,null=False)
    current_order = models.IntegerField()

class orders(models.Model):
    table = models.ForeignKey(tables,on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,blank=False,null=False,choices=STATUS_CHOICES,default="ongoing")
    timestamp = models.TimeField()

class ordersdetail(models.Model):
    order = models.ForeignKey(orders,on_delete=models.DO_NOTHING) 
    menu = models.ForeignKey(MenuItems,on_delete=models.DO_NOTHING)
    numbers = models.IntegerField()
    subtotal_price = models.DecimalField(max_digits=7,decimal_places=2)

class receipts(models.Model):
    order = models.OneToOneField(orders)
    total_price = models.DecimalField(max_digits=7,decimal_places=2)
    final_price = models.DecimalField(max_digits=7,decimal_places=2)
    timestamp = models.TimeField()