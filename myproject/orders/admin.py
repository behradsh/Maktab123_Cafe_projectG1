from django.contrib import admin
from .models import Tables,Orders,OrdersDetails,Reciepts
# Register your models here.
@admin.register(Tables)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number","current_order","status")
    list_filter = ["table_number","status"]

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("table","customer","status","timestamp",)
    list_filter = ["table","customer","status","timestamp"]

@admin.register(OrdersDetails)
class OrdersDetailsAdmin(admin.ModelAdmin):
    list_display = ("order","menu","numbers","subtotal_price")
    list_filter = ["order","menu","numbers","subtotal_price"] 

@admin.register(Reciepts)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("order","total_price","final_price","timestamp")
    list_filter = ["order","total_price","final_price"]