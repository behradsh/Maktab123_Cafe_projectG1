from django.contrib import admin
from .models import Customers, Message
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'role')
    search_fields = ['first_name', 'last_name', 'email']

class MessageAdmin(admin.ModelAdmin):
    list_display = ('description', 'user')
    search_fields = ['description']
    list_filter = ['user']
    
    
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Message, MessageAdmin)