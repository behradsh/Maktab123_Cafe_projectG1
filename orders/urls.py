from django.urls import path
from . import views

urlpatterns = [
    path("order_detail/",views.OrderDetail.as_view(),name="order_detail"),
    path("general_order/",views.OrderDetail.as_view(),name="order"),
    path("receipt/",views.Receipt.as_view(),name="receipt"),
]