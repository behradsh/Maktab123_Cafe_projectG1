from django.urls import path,include
from .views import (
    login_user_view,
    LogOutView,
    profile,
    send_message,
    home_view,
    home_farsi_view,
    about_view,
    register_user_view,
    dashboard_view,
    dashboard_message_view,

)

urlpatterns = [
    path('',home_view, name='home'),
    path('home_farsi',home_farsi_view, name='home_farsi'),
    path('about/',about_view,name='about'),
    path('dashboard/',dashboard_view,name='admin-dashboard'),
    path('dashboard/messages',dashboard_message_view,name='messages'),
    path('dashboard/', include('orders.urls')),
    path('login/',login_user_view,name='login'),
    path('register/',register_user_view,name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('admin/profile/', profile, name='profile'),
    path('admin/messages/', send_message, name='send_message'),
     # path('admin/view-messages/', view_messages, name='view_messages'),
]
