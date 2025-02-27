from django.db import models
from menu.models import MenuItems
from customer.models import Customers

RECIEPT_STATUS_CHOICES = (
    ("pending", "pending"),
    ("paid", "paid"),)
STATUS_CHOICES = (
        ("waiting", "waiting"),
        ("cooking", "cooking"),
        ("served", "served"))
TABLE_STATUS_CHOICES = (("empty","empty"),
                ("fill","fill"),)
# Create your models here.
class Tables(models.Model):
    table_number = models.IntegerField(unique=True,null=False,blank=False)
    current_order = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=TABLE_STATUS_CHOICES, default="empty",editable=True)

    class Meta:
        verbose_name_plural = "Tables"

    def __str__(self):
        return f"{self.table_number}"

class Orders(models.Model):
    table = models.ForeignKey(Tables,on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,blank=False,null=False,choices=STATUS_CHOICES,default="ongoing")
    timestamp = models.TimeField()
    class Meta:
        verbose_name_plural = "Orders"

class OrdersDetails(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(MenuItems,on_delete=models.DO_NOTHING)
    numbers = models.IntegerField()
    subtotal_price = models.DecimalField(max_digits=7,decimal_places=2)
    class Meta:
        verbose_name_plural = "OrderDetails"

class Reciepts(models.Model):
    order = models.OneToOneField(Orders,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7,decimal_places=2)
    final_price = models.DecimalField(max_digits=7,decimal_places=2)
    status = models.CharField(max_length=100,blank=False,null=False,choices=RECIEPT_STATUS_CHOICES,default="pending")
    timestamp = models.TimeField()
    class Meta:
        verbose_name_plural = "Reciepts"