from django.shortcuts import render
from django.http import HttpResponse
from base.models import Customer
from order.models import Order

def homee(request):
    if request.session.get('custid'):
        custid=request.session.get('custid')
        user=Customer.objects.get(custid=custid)
        order = Order.objects.filter(user=request.user).first()
        return render(request, "home.html",{'user':user}, {"order": order})
    return render(request, "home.html")