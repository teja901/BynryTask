from django.urls import path
from .views import *

urlpatterns = [
   
    path('homepage',home_page,name='homepage'),
    path('customer_register',customer_register,name='customer_register'),
    path('login',customer_login,name='customerlogin'),
    path('customerprofile',customer_profile,name='customerprofile'),
    path('customer_LogOut',customer_LogOut,name='customer_LogOut'),
]