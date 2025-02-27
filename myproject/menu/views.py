from django.shortcuts import render
from .models import MenuItems, Category
from django.shortcuts import get_object_or_404
# Create your views here.
#Display Menu Items

def menu(request):
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
    item = get_object_or_404(MenuItems, id = item_id) #Specific menu item
    context = {'item': item}
    return render(request, 'item_details.html', context)

#Add to cart
def add_to_cart(request, item_id):
    pass