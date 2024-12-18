from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True, default=1)  # Auto-increment primary key field
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    owner_name = models.CharField(max_length=255,default="Default Owner Name")
    shop_name = models.CharField(max_length=255,)
    shop_address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, default="", blank=True)

    def __str__(self):
        return f"{self.shop_name} - {self.owner_name}"   
    
class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return self.name