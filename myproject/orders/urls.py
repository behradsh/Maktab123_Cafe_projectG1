from django.urls import path,include
from .views import (tables_list_view,
                    tables_create_view,
                    tables_update_view,
                    table_delete_view)
urlpatterns = [
    path('tables/',tables_list_view,name='tables_list'),
    path('table/add/',tables_create_view,name='table_create'),
    path('table/<int:table_id>/',tables_update_view,name='table_update'),
    path('table/<int:table_id>/delete',table_delete_view,name='table_delete'),
]