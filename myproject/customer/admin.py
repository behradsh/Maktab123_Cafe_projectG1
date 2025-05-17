from django.contrib import admin
from .models import Customers, Message
# Register your models here.
admin.site.register(Message)

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    fields = [("username","email","password","role","is_staff"),("first_name","last_name","phone_number")]
    list_display = ("username","email","first_name","last_name","phone_number")
    list_filter = ["id","first_name","last_name"]    