from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Customers(AbstractUser):
    ROLE_CHOICES =[
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank= True)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique= True)
    password = models.CharField(max_length=128)
    birth_date = models.DateField(null = True, blank= True)
    role = models.CharField(max_length= 10, choices= ROLE_CHOICES, default= 'customer' )
    username = models.CharField(max_length=150, unique= True, default= 'default_username')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name= 'customer_groups',
        blank= True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name = 'customers_user_permissions',
        blank= True,
    )
class Message(models.Model):
    description = models.TextField()
    user = models.ForeignKey(Customers, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    