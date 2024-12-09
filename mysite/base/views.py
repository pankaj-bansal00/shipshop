from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages
from base.models import Customer
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if email already exists
        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('signup')  # Redirect back to the signup page

        # Create the user
        user = Customer.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')  # Redirect to the login page after successful signup
    
    return render(request, "register/signup.html")  


def user_login(request):  # Renamed from login to avoid conflict
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # Authenticate user using username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User authenticated:")
            auth_login(request, user)  # Using auth_login to avoid conflict
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'register/login.html')

def user_logout(request):
    auth_logout(request)  # Properly log out the user
    return redirect('home')  # Redirect to the homepage or login page after logging ou