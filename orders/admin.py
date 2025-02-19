from django.contrib import admin
from .models import tables,orders,ordersdetail,receipts
# Register your models here.
@admin.register(tables)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number","cafe_space_position","current_order",)
    list_filter = ["table_number","cafe_space_position"]

@admin.register(orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("table","customer","status","timestamp",)
    list_filter = ["table","customer","status","timestamp"]

@admin.register(ordersdetail)
class OrderdetailAdmin(admin.ModelAdmin):
    list_display = ("order","menu","numbers","subtotal_price")
    list_filter = ["order","menu","numbers","subtotal_price"] 

@admin.register(receipts)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("order","total_price","final_price","timestamp")
    list_filter = ["order","total_price","final_price"]       