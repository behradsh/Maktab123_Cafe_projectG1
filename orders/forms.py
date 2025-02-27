from django import forms
from .models import Orders,OrdersDetails,Receipts

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrdersDetails
        fields = ['order','menu','numbers']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['table','customer','status']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = ['order','total_price','final_price']                        