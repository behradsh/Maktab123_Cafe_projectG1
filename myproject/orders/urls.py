from django.urls import path,include
from .views import (tables_list_view,
                    tables_create_view,
                    tables_update_view,
                    table_delete_view,
                    show_order_list,
                    order_details_list,
                    order_update_view,
                    order_delete_view,
                    create_order_view,
                    create_orderdetail,
                    delete_orderdetail,
                    edit_orderdetail,
                    receipt_show_list,
                    create_receipt,
                    update_receipt,
                    delete_receipt)
from menu.views import admin_menu ,admin_menu_farsi, add_menu_item , edit_menu_item , delete_menu_item 

urlpatterns = [
    path('tables/',tables_list_view,name='tables_list'),
    path('table/add/',tables_create_view,name='table_create'),
    path('table/<int:table_id>/',tables_update_view,name='table_update'),
    path('table/<int:table_id>/delete',table_delete_view,name='table_delete'),
    
    path('menu_items' , admin_menu , name='admin_menu') ,
    path('menu_items/farsi/', admin_menu_farsi, name='admin_menu_farsi'),
    path('menu_item/add/' , add_menu_item , name='add_menu_item'),
    path('menu_item/<int:item_id>' , edit_menu_item , name='edit_menu_item'),
    path('menu_item/<int:item_id>/delete' , delete_menu_item , name='delete_menu_item'),

    path("orders/",show_order_list,name="orders"),
    # path("order/<int:order_id>",show_order_indetail,name="order"),
    path("create_order/",create_order_view,name="create_order"),
    path("edit_order/<int:order_id>",order_update_view,name="update_order"),
    path("delete_order/<int:order_id>",order_delete_view,name="delete_order"),

    path("order_details/",order_details_list,name="order_details"),
    # path("order_detail/<int:orderdetail_id>",order_details_indetail,name="order_detail"),
    path("create_order_detail/",create_orderdetail,name="create_order_detail"),
    path("edit_order_detail/<int:orderdetail_id>",edit_orderdetail,name="orderdetail_edit"),
    path("delete_order_detail/<int:orderdetail_id>",delete_orderdetail,name="delete_orderdetail"),

    path("receipts/",receipt_show_list,name="receipt_list"),
    # path("receipt/<int:receipt_id>",receipt_show_indetail,name="receipt"),
    path("create_receipt/",create_receipt,name="create_receipt"),
    path("edit_receipt/<int:receipt_id>",update_receipt,name="edit_receipt"),
    path("delete_receipt/<int:receipt_id>",delete_receipt,name="delete_receipt"),
]