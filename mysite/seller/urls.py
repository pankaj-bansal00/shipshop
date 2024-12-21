from django.urls import path
from . import views
from .views import add_product, seller_dashboard, delete_product, edit_product
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.shortcuts import redirect


urlpatterns = [     
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('seller_login/', views.seller_login, name='seller_login'),
    path('seller_logout/', views.seller_logout, name='seller_logout'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),      
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('search/', views.search_view, name='search'), 
    path('category/<slug:category_slug>/', views.category_view, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)