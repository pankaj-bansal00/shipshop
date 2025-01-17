from django.shortcuts import render
from django.http import HttpResponse
from base.models import Customer
from order.models import Order
from seller.models import Category

def homee(request):
    Categorys = Category.objects.all()
    if request.session.get('custid'):
        custid=request.session.get('custid')
        user=Customer.objects.get(custid=custid)
        order = Order.objects.filter(custid=custid).first()     
        return render(request, "home.html",{'user':user, 'Categorys':Categorys})
    return render(request, "home.html", {'Categorys':Categorys})