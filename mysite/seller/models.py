from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=200)
    seller_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name