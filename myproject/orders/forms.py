from django import forms
from .models import Tables,Orders,OrdersDetails,Reciepts

class TablesForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = '__all__'

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"
        exclude = ["timestamp"]

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrdersDetails
        fields = "__all__" 


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Reciepts
        fields = "__all__"
        exclude = ["timestamp"]
        