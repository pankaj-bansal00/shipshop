from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from seller.models import Product, Seller, Product, Category  # Ensure Seller is imported
from django.http import JsonResponse
from seller.models import Seller
@login_required
def add_product(request):
    # Check if the user is a seller
    if not hasattr(request.user, 'seller'):  # Adjusted this to 'seller' instead of 'seller_profile'
        messages.error(request, "You must be a seller to add products.")
        return redirect('seller_dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_product':
            # Handle adding product
            name = request.POST.get('name')
            category_id = request.POST.get('category')
            price = request.POST.get('price')
            description = request.POST.get('description')
            photo = request.FILES.get('photo')

            if not all([name, category_id, price, description]):
                messages.error(request, "All fields are required.")
            else:
                try:
                    category = category.objects.get(id=category_id)
                    seller = request.user.seller  # Adjusted to use 'seller'
                    product = product.objects.create(
                        seller=seller,
                        name=name,
                        category=category,
                        price=price,
                        description=description,
                        photo=photo
                    )
                    messages.success(request, "Product added successfully!")
                    return redirect('seller_dashboard')
                except category.DoesNotExist:
                    messages.error(request, "Selected category does not exist.")
        
        elif action == 'add_category':
            # Handle adding category
            category_name = request.POST.get('category-name')
            category_image = request.FILES.get('category-image')

            if not category_name or not category_image:
                return JsonResponse({'error': 'Both name and image are required'}, status=400)
            
            category = category.objects.create(name=category_name, image=category_image)
            categories = category.objects.all()
            return render(request, 'seller/add_product.html', {'categories': categories})
    
    categories = category.objects.all()
    return render(request, 'seller/add_product.html', {'categories': categories})


@login_required
def seller_dashboard(request):
    if not hasattr(request.user, 'seller'):  # Adjusted to check 'seller' profile
        messages.error(request, "You must be a seller to view this page.")
        return redirect('seller_dashboard')

    seller = request.user.seller  # Adjusted to use 'seller'
    products = seller.product_set.all()  # Using product_set to access related products
    return render(request, 'seller/seller_dashboard.html', {'products': products})

# Further views (like delete_product, edit_product, etc.) should be updated similarly.


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(product, id=product_id, seller=request.user.seller_profile)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('seller_dashboard')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user.seller_profile)
    if request.method == 'POST':
        # Update product fields here
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect('seller_dashboard')
    return render(request, 'edit_product.html', {'product': product})

def search_view(request):
    query = request.GET.get('q')  # 'q' is the name of the input field
    products = Product.objects.filter(name__icontains=query) if query else None
    return render(request, 'search_results.html', {'products': products, 'query': query})


def category_view(request, category_slug):
    category = get_object_or_404(category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})
