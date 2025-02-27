from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import TablesForm
from .models import Tables
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
    # table_obj = Tables.objects.get(id=table_id)
    table_obj = get_object_or_404(Tables,id=table_id)
    if request.method == "POST":
        table_obj.delete()
        return HttpResponseRedirect("/dashboard/tables")
    return render(request,"dashboard/table_delete.html",context)