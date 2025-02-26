from django import forms
from .models import Orders,OrdersDetails,Tables,Receipts

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrdersDetails
        fields = ['order','menu','numbers']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['table','customer','status']

class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['table_number','cafe_space_position','current_order']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = ['order','total_price','final_price']                        