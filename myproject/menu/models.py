from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
    
class Category(models.Model):
    title = models.CharField(max_length= 100)
    class Meta:
        verbose_name_plural = "Categories"


class MenuItems(models.Model):

    name = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], default=0)
    serving_time_period = models.PositiveIntegerField()
    estimated_cooking_time = models.PositiveIntegerField()
    description = models.TextField(blank=True , null=True)
    image = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Menu Items"

