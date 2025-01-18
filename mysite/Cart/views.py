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
    # Validate the customer
    custid = request.session.get('custid')
    user = get_object_or_404(Customer, custid=custid)

    # Get the product
    product = get_object_or_404(Product, Productid=product_id, is_available=True)

    # Get or create the cart
    cart, created = Cart.objects.get_or_create(user=user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Increment the quantity if already exists
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_view')

def checkout_view(request):
    # Fetch the customer ID from the session
    custid = request.session.get('custid')
    if not custid:
        return redirect('login')  # Redirect to login if no customer ID is found in the session

    try:
        # Fetch the user object using the custid
        user = Customer.objects.get(custid=custid)
        # Retrieve the cart for the user
        cart = Cart.objects.get(user=user)
    except (Customer.DoesNotExist, Cart.DoesNotExist):
        # Handle cases where the customer or cart does not exist
        return redirect('cart_view')  # Redirect to a cart view or error page

    # Render the checkout page
    return render(request, 'checkout.html', {'cart': cart})


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
