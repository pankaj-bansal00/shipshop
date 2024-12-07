from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Customer(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username