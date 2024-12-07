from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your models here.

class signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name