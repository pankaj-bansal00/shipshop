from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your models here.
class Customer(models.Model):
    custid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
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

    def save(self, *args, **kwargs):
        # Hash password before saving
        if not self.pk:  # Only hash for new records
            self.password = make_password(self.password)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
