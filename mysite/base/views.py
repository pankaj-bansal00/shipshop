from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from seller.models import Seller
from django.contrib.auth.hashers import make_password
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        mobile_number = request.POST['mobile_number']

        print(username)
        # Check if email already exists
        if User.objects.filter(email=email,mobile_number=mobile_number).exists():
            messages.error(request, 'Email is already registered')
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, 
                password=password, 
                email=email, 
                mobile_number=mobile_number, 
                )
            user.save()
            print("success")
            return redirect('login')  # Redirect to the login page after successful signup
        except Exception as e:
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

