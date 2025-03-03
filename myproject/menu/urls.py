from django.urls import path
from .views import admin_menu , customer_menu ,menu_search, menu_filter, item_detail, add_to_cart , edit_menu_item , delete_menu_item , add_menu_item

urlpatterns = [
    path('', customer_menu, name='menu'),  
    # path('admin/menu/', admin_menu, name='admin_menu' ),
    path('item/<int:item_id>/', item_detail, name='item_detail'),  
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),  
    path('search/' , menu_search , name='menu_search'),
    path('filter/' , menu_filter , name='menu_filter'),
    # path('add/' , add_menu_item , name='add_menu_item'),
    # path('edit/<int:item_id>' , edit_menu_item , name='edit_menu_item'),
    # path('delete/<int:item_id>' , delete_menu_item , name='delete_menu_item'),
]