from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import CartItem,Cart
from seller.models import Product
from base.models import Customer
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# def cart_view(request):
#     cart = Cart.objects.get(user=request.user)
#     return render(request, 'cart/cart.html', {'cart': cart})
from django.contrib.auth import get_user_model
User = get_user_model()
def cart_view(request):
    if request.session.get('custid'):
        # Try to get the cart for the user
        try:
            custid = request.session.get('custid')
            user = Customer.objects.get(custid=custid)
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            # If the cart does not exist, create a new one
            cart = Cart.objects.create(user=user)

        # Proceed with your logic (e.g., displaying the cart)
        return render(request, 'cart.html', {'cart': cart})
    else:
        # Redirect to login or show an error
        return redirect('login')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, Customer=request.session.get('custid'), is_available=True)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_view')

def checkout_view(request):
    cart = Cart.objects.get(user=request.user)
    # Placeholder logic for the checkout process
    return render(request, 'cart/checkout.html', {'cart': cart})


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart_view')

def update_cart(request, item_id):
    if request.method == "POST":
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.quantity = request.POST.get('quantity', cart_item.quantity)
        cart_item.save()
    return redirect('cart_view')
