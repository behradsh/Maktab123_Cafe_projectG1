from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Orders,OrdersDetails,Tables,Receipts
from .forms import OrderDetailForm,OrderForm,TableForm,ReceiptForm
from django.views.generic import UpdateView,DeleteView
from django.shortcuts import get_object_or_404

class OrderDetail(View):
    def get(self,request,*args,**kwargs):
        context = get_object_or_404(OrdersDetails,id=kwargs)
        return render(request,'order_detail.html',context=context)

    def post(self,request,*args,**kwargs):
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else :
            sample_form = OrderDetailForm()
            return render(request,'order_detail.html',context={"form":sample_form})

class OrderDetailUpdate(UpdateView): 
    model = OrdersDetails
    form = OrderDetailForm
    template_name = 'order_detail.html'


class DeleteOrderDetail(DeleteView):   
    model = OrdersDetails
    template_name = 'order_detail_delete.html'
    

class Order(View):
    def get(self,request,*args,**kwargs):
        context = get_object_or_404(Orders,id=kwargs)
        return render(request,'order.html',context=context)

    def post(self,request,*args,**kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipt')
        else :
            sample_form = OrderForm()
            return render(request,'order.html',context={"form":sample_form})

class OrderUpdate(UpdateView): 
    model = Orders
    form = OrderForm
    template_name = 'order.html'


class DeleteOrder(DeleteView):   
    model = Orders
    template_name = 'order_delete.html'
    

class Receipt(View):
    def get(self,request,*args,**kwargs):
        context = get_object_or_404(Receipts,id=kwargs)
        return render(request,'receipt.html',context=context)

    def post(self,request,*args,**kwargs):
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else :
            sample_form = ReceiptForm()
            return render(request,'receipt.html',context={"form":sample_form})

class ReceiptUpdate(UpdateView): 
    model = Receipts
    form = ReceiptForm
    template_name = 'receipt.html'


class DeleteReceipt(DeleteView):   
    model = Receipts
    template_name = 'delete_receipt.html'    

class Table(View):
    def get(self,request,*args,**kwargs):
        context = get_object_or_404(Tables,id=kwargs)
        return render(request,'table.html',context=context)

    def post(self,request,*args,**kwargs):
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_detail')
        else :
            sample_form = TableForm()
            return render(request,'table.html',context={"form":sample_form})

class OrderDetailUpdate(UpdateView): 
    model = Tables
    form = TableForm
    template_name = 'table.html'


class DeleteOrderDetail(DeleteView):   
    model = Tables
    template_name = 'table_delete.html'    




# Create your views here.
