from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from seller.models import Product, Seller, Category  
from django.http import JsonResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.hashers import make_password
""" Create An Account For Seller """

def seller_signup(request):
    if request.method == 'POST':
        owner_name = request.POST.get('owner_name')
        shop_name = request.POST.get('shop_name')
        shop_address = request.POST.get('shop_address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register/seller_signup.html')

        try:
            seller = Seller.objects.create(
                owner_name=owner_name,
                shop_name=shop_name,
                shop_address=shop_address,
                email=email,                
                phone=phone,
                password=password  # Will be hashed in the `save` method
            )
            seller.password = make_password(password)
            seller.save()
            messages.success(request, "Seller account created successfully!")
            return redirect('seller_login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
    
    return render(request, 'register/seller_signup.html') 

""" Login For Seller """
def seller_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("Attempting login for:", email)

        try:
            # Check if a seller with the given email exists
            seller = Seller.objects.get(email=email)
            if check_password(password, seller.password):  # Verify password
                request.session['seller_id'] = seller.seller_id  # Store seller in session
                messages.success(request, "Logged in successfully!")
                print("Login successful, redirecting to dashboard...")
                return redirect('seller_dashboard')  # Redirect to seller dashboard
            else:
                print("Invalid credentials: Password mismatch")
                messages.error(request, "Invalid credentials. Please try again.")
        except Seller.DoesNotExist:
            print("Seller with email not found:", email)
            messages.error(request, "No seller account found with this email.")
    
    return render(request, 'register/seller_login.html')

""" Dashboard For Seller """

def seller_dashboard(request):
    seller_id = request.session.get('seller_id')
    if not seller_id:
        messages.error(request, "You must log in to access the dashboard.")
        return redirect('seller_login')
    products = Product.objects.filter(seller_id=seller_id)  
    seller = Seller.objects.get(seller_id=seller_id) 
    return render(request, 'seller/seller_dashboard.html', {'seller': seller, 'products': products})

def seller_logout(request):
    if 'seller_id' in request.session:  
        del request.session['seller_id']  # Remove seller ID from session
    messages.success(request, "Logged out successfully.")
    return redirect('seller_login')

# Further views (like delete_product, edit_product, etc.) should be updated similarly.
""" Add Product """

def add_product(request):

    categories = Category.objects.all()
    if request.session.get('seller_id'):
        seller_id = request.session.get('seller_id')
        seller = Seller.objects.get(seller_id=seller_id)  
        if request.method == 'POST':    
            name = request.POST.get('name')          
            price = request.POST.get('price')
            description = request.POST.get('description')
            photo = request.FILES.get('photo')
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            product = Product.objects.create(seller=seller, name=name, price=price, description=description, photo=photo, category=category)
            product.save()  
            return redirect('seller_dashboard')  
        return render(request, 'seller/add_product.html', {'seller': seller, 'categories': categories})       
    else:
        messages.error(request, "You must log in to add products.")
        print("You must log in to add products.")
        return redirect('seller_login')
    

    
def delete_product(request, product_id):
    sellerid = request.session.get('seller_id')
    seller = Seller.objects.get(seller_id=sellerid)     
    product = get_object_or_404(Product, Productid=product_id, seller=seller)    
    product.delete()
    print("Product deleted successfully.")
    messages.success(request, "Product deleted successfully.")  
    return redirect('seller_dashboard')
def edit_product(request, product_id):
    sellerid = request.session.get('seller_id')
    seller = Seller.objects.get(seller_id=sellerid)     
    product = get_object_or_404(Product, Productid=product_id, seller=seller)
    if request.method == 'POST':
        # Update product fields here
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect('seller_dashboard')
    return render(request, 'seller/edit_product.html', {'product': product})


def search_view(request):
    query = request.GET.get('q')  # 'q' is the name of the input field
    products = Product.objects.filter(name__icontains=query) if query else None
    return render(request, 'search_results.html', {'products': products, 'query': query})


def category_view(request, category_slug):
    category = get_object_or_404(category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})
