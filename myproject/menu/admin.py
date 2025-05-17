from django.contrib import admin
from .models import MenuItems, Category
# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin) :
    list_display = ('name' ,'price' ,'category' , 'discount' ,'serving_time_period' , 'estimated_cooking_time' )
    search_fields = ('name' ,'category')
    list_filter = ('category' ,'discount')


admin.site.register(MenuItems , MenuItemsAdmin)
admin.site.register(Category)