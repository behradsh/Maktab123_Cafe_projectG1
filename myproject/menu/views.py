from django.shortcuts import render , redirect
from .models import MenuItems, Category
from django.shortcuts import get_object_or_404
from .forms import MenuItemForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import activate
from django.http import HttpResponseRedirect,HttpResponseBadRequest
# Create your views here.

#Display Menu Items for admin's english
@login_required
def admin_menu(request):
    if not request.user.is_staff:
        return redirect('menu')
    items = MenuItems.objects.all()
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'menu/dashboard_menu.html', context)

#Display Menu Items for admin's farsi
@login_required
def admin_menu_farsi(request):
    if not request.user.is_staff:
        return redirect('menu')
    items = MenuItems.objects.all()
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'menu/dashboard_menu_farsi.html', context)

#Display Menu Items for customer's
def customer_menu(request):
    items = MenuItems.objects.all()
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'menu/menu.html', context)

#Filter Menu Items
def menu_filter(request):
    category = request.GET.get('category', None) #select category from query params
    if category:
        items = MenuItems.objects.filter(category = category)
    else:
        items = MenuItems.objects.all()
    categories = Category.objects.all()
    context = {'items': items , 'categories' : categories }
    return render(request, 'menu/menu.html', context)

#Search Menu Items
def menu_search(request):
    query = request.GET.get('q', '')  # Get search query from input
    items = MenuItems.objects.filter(name__icontains=query)
    categories = Category.objects.all()
    context = {'items': items,'categories' : categories ,'query': query}
    return render(request, 'menu/menu.html', context)

#Item Details View
def item_detail(request, item_id):
    item = get_object_or_404(MenuItems, id=item_id) #Specific menu item
    context = {'item': item}
    return render(request, 'menu/item_details.html', context)

#Add to cart
def add_to_cart(request, item_id):
    pass

#Add Menu Item
@login_required
def add_menu_item (request) :
    if request.method == 'POST' :
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_menu')
        else :
            return HttpResponseBadRequest()
    else :
        form = MenuItemForm()
    
    return render(request , 'menu/add_menu_item.html' , {'form' : form})



#Edit Menu Item
@login_required
def edit_menu_item(request , item_id) :
    menu_item = get_object_or_404(MenuItems , id=item_id)
    if request.method =='POST' :
        form = MenuItemForm(request.POST , instance=menu_item)
        if form.is_valid() :
            form.save()
            return redirect('admin_menu')
        else :
            return HttpResponseBadRequest()
    else :
        form = MenuItemForm(instance=menu_item)
        
    return render(request , 'menu/edit_menu_item.html' , {'form' : form , 'menu_item' : menu_item})
    

#Delete Menu Item
@login_required
def delete_menu_item(request , item_id) :
    menu_item = get_object_or_404(MenuItems , id=item_id)

    if request.method == 'POST':
        menu_item.delete()
        return redirect('admin_menu')
    return render (request , 'menu/delete_menu_item.html' , {'menu_item' : menu_item})