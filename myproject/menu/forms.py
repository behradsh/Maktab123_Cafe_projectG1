from django import forms
from .models import MenuItems


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems 
        fields = ['name', 'price', 'category', 'discount', 'serving_time_period', 'estimated_cooking_time', 'description']