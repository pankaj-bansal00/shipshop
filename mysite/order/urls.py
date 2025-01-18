from django.urls import path
from . import views

urlpatterns = [
    path('place-order/<slug:slug>/', views.place_order, name='place_order'),
    path('order-success/<slug:slug>/', views.order_success, name='order_success'),
]