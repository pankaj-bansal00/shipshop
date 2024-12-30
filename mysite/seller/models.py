from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from autoslug import AutoSlugField
from django.core.validators import RegexValidator


class Seller(models.Model):     
    seller_id = models.AutoField(primary_key=True,)  # Auto-increment primary key field
    owner_name = models.CharField(max_length=255, default="Default Owner Name")
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=10,
        unique=True,
        default='0000000000',
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Mobile number must be exactly 10 digits.",
                code='invalid_mobile_number'
            )
        ]
    )
    password = models.CharField(max_length=255, default="")  # Store hashed passwords

    def save(self, *args, **kwargs):
        if not self.pk and self.password:  # Hash password only on creation
            self.password = make_password(self.password)
        super(Seller, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.shop_name} - {self.owner_name}"

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products', null=True, blank=True)  # Link to Seller
    Productid = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')                  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', unique=True)
    photo = models.ImageField(upload_to='products/', blank=True, null=True, ) 

    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name