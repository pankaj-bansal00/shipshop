from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractUser, User, Group, Permission


# Create your models here.

class Customer(models.Model):
    custid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.IntegerField(default=None, unique=True, null=True, blank=True)

    

    def __str__(self):
        return self.username
