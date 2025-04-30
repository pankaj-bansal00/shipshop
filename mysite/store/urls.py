from django.urls import path
from store import views
from django.urls import include

urlpatterns = [
    path('product/<int:productid>/', views.product_detail_view, name='product_detail'),
]
