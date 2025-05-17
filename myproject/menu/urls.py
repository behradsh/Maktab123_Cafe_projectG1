from django.urls import path
from .views import customer_menu ,menu_search, menu_filter, item_detail, add_to_cart

urlpatterns = [
    path('', customer_menu, name='menu'),  
    # path('admin/menu/', admin_menu, name='admin_menu' ),
    path('item/<int:item_id>/', item_detail, name='item_detail'),  
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),  
    path('search/' , menu_search , name='menu_search'),
    path('filter/' , menu_filter , name='menu_filter'),
]