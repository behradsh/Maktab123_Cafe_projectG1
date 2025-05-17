from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect , HttpResponseBadRequest
from .forms import TablesForm,OrdersForm,OrderDetailsForm,ReceiptForm
from .models import Tables,Orders,OrdersDetails,Reciepts
from .forms import TablesForm,OrdersForm,OrderDetailsForm,ReceiptForm
from .models import Tables,Orders,OrdersDetails,Reciepts
# Create your views here.

def tables_list_view(request):
    tables = Tables.objects.all()
    context = {'tables':tables}
    return render(request,"dashboard/dashboard_tables.html",context)


def tables_create_view(request):
    if request.method == "POST":
        form = TablesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tables_list")
    else:
        form = TablesForm()
    return render(request,"dashboard/table_create.html",{"form":form})

def tables_update_view(request,table_id):
    context = {}
    table_obj = Tables.objects.get(id=table_id)
    form = TablesForm(instance=table_obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/dashboard/tables/")
    context['form'] = form
    return render(request,"dashboard/table_update.html",context)

def table_delete_view(request,table_id):
    context = {}
    table_obj = get_object_or_404(Tables,id=table_id)
    if request.method == "POST":
        table_obj.delete()
        return HttpResponseRedirect("/dashboard/tables")
    return render(request,"dashboard/table_delete.html",context)

def show_order_list(request):
    orders_obj = Orders.objects.all()
    context = {"orders":orders_obj}
    return render(request,"orders/orders.html",context=context)

def show_order_indetail(request,order_id):
    orders_indetail_obj = Orders.objects.get(id=order_id)
    context = {"order":orders_indetail_obj}
    return render(request,"orders/",context=context)

def create_order_view(request):
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("orders")
        else :
            return HttpResponseBadRequest()
    else:
        form = OrdersForm()
    return render(request,"orders/create_order.html",{"form":form})

def order_update_view(request,order_id):
    context = {}
    order_obj = Orders.objects.get(id=order_id)
    form = OrdersForm(instance=order_obj)
    if form.is_valid():
        form.save()
        redirect("orders")
    context['form'] = form
    return render(request,"orders/edit_order.html",context)   

def order_delete_view(request,order_id):
    context = {}
    order_obj = get_object_or_404(Orders,id=order_id)
    if request.method == "POST":
        order_obj.delete()
        redirect("orders")
    return render(request,"orders/delete_order.html",context=context)

def order_details_list(request):
    order_details_obj = OrdersDetails.objects.all()
    context = {"orderdetails":order_details_obj}
    return render(request,"orders/orderdetails.html",context=context)

def order_details_indetail(request,orderdetail_id):
    order_details_obj = OrdersDetails.objects.get(id=orderdetail_id)
    context = {"orderdetail":order_details_obj}
    return render(request,"orders/",context=context)

def create_orderdetail(request):
    if request.method == "POST":
        form = OrderDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("order_details")
        else:
            return HttpResponseBadRequest()    
    else :
        form = OrderDetailsForm()  

    return render(request,"orders/create_orderdetail.html",{"form":form})    

def edit_orderdetail(request,orderdetail_id):
    context = {}
    orderdetail_obj = OrdersDetails.objects.get(id=orderdetail_id)
    form = OrderDetailsForm(instance=orderdetail_obj)
    if form.is_valid():
        form.save()
        redirect("order_details")
    context['form'] = form
    return render(request,"orders/edit_orderdetail.html",context=context)    

def delete_orderdetail(request,orderdetail_id):
    context = {}
    orderdetail_obj = get_object_or_404(OrdersDetails,id=orderdetail_id)
    if request.method == "POST":
        orderdetail_obj.delete()
        HttpResponseRedirect("orders/order_details/")
    return render(request,"orders/delete_orderdetail.html",context=context)  

def receipt_show_list(request):
    receipts_obj = Reciepts.objects.all()
    context = {"receipts":receipts_obj}
    return render(request,"orders/receipts.html",context=context)

def receipt_show_indetail(request,receipt_id):
    receipt_obj = Reciepts.objects.get(id=receipt_id)
    context = {"receipts":receipt_obj}
    return render(request,"orders/",context=context)

def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("receipt_list")
        else:
            return HttpResponseBadRequest()    
    else:
        form = ReceiptForm()
    return render(request,"orders/create_receipt.html",{"form":form})     

def update_receipt(request,receipt_id):
    context = {}
    receipt_obj = Reciepts.objects.get(id=receipt_id)
    form = ReceiptForm(instance=receipt_obj)
    if form.is_valid():
        form.save()
        redirect("receipt_list")
    context['form'] = form
    return render(request,"orders/edit_receipt.html",context)

def delete_receipt(request,receipt_id):
    context = {}
    receipt_obj = get_object_or_404(Reciepts,id=receipt_id)
    if request.method == "POST":
        receipt_obj.delete()
        redirect("receipt_list")
    return render(request,"orders/delete_receipt.html",context=context)
