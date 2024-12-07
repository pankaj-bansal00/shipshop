from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

# Create your views here.

def login(request):  
    
    
    return render(request,"register/login.html")

"""def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # Authenticate the user
            if user is not None:
                login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page
    else:
        form = UserCreationForm()  # Initialize an empty form for GET request

    # Render the form with context
    return render(request, "register/signup.html", {'form': form})"""

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("sucess")
    
    return render(request, "register/signup.html")  