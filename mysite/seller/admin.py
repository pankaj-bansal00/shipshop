from django.contrib import admin
from seller.models import Seller
from django.contrib.auth.admin import UserAdmin
from seller.models import Product, Category

# Register your models here.
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Category)