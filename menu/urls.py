from django.urls import path
from .views import menu, menu_search, menu_filter, item_detail, add_to_cart

urlpatterns = [
    path('', menu, name='menu'),  # URL for the menu page
    path('item/<int:item_id>/', item_detail, name='item_detail'),  # URL for item detail
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),  # URL to add item to cart
    path('search/' , menu_search , name='menu_search'),
    path('filter/' , menu_filter , name='menu_filter'),
]