from django.contrib import admin
from seller.models import Seller
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Seller)