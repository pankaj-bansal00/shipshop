from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from seller.models import Seller
from .models import Customer
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        print(f"Username: {username}, Email: {email}, Password: {password}, Confirm Password: {confirm_password}, Phone: {phone}")
        
        # # Check for missing fields
        # if not username or not email or not password or not confirm_password or not phone:  
        #     messages.error(request, "All fields are required")
        #     print("All fields are required")
        #     return redirect('signup')

        # Validate passwords match
        if password != confirm_password:
            print("Passwords do not match")
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # Check if email or mobile number already exists
        # if User.objects.filter(email=email).exists():
        #     print("Email is already registered")
        #     messages.error(request, "Email is already registered")
        #     return redirect('signup')
        # if User.objects.filter(phone=phone).exists():
        #     print("Mobile number is already registered")
        #     messages.error(request, "Mobile number is already registered")
        #     return redirect('signup')

        try:
            print("Creating user account...")
            user = Customer.objects.create(
                username=username,
                email=email,
                phone=phone,
                password=password
            )
            user.password = make_password(password)
            print("User account created successfully...")
            user.save()
            print("Account created successfully")
            messages.success(request, "Account created successfully")
            return redirect('login')  # Redirect to login
        except Exception as e:
            print(f"Error creating account: {str(e)}")
            messages.error(request, f"Error creating account: {str(e)}")

    
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


def logout(request):
    auth_logout(request)
    return redirect('home')  # Replace 'home' with the name of your desired redirect URL.

