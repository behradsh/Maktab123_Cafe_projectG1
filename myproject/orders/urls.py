from django.urls import path,include
from .views import (tables_list_view,
                    tables_create_view,
                    tables_update_view,
                    table_delete_view)
from menu.views import admin_menu , add_menu_item , edit_menu_item , delete_menu_item
urlpatterns = [
    path('tables/',tables_list_view,name='tables_list'),
    path('table/add/',tables_create_view,name='table_create'),
    path('table/<int:table_id>/',tables_update_view,name='table_update'),
    path('table/<int:table_id>/delete',table_delete_view,name='table_delete'),
    
    path('menu_items' , admin_menu , name='admin_menu') ,
    path('menu_item/add/' , add_menu_item , name='add_menu_item'),
    path('menu_item/<int:item_id>' , edit_menu_item , name='edit_menu_item'),
    path('menu_item/<int:item_id>/delete' , delete_menu_item , name='delete_menu_item'),
]