# task4/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop/', views.shop_view, name='shop'),
    path('cart/', views.cart_view, name='cart'),
]
