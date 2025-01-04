from django.shortcuts import render
from django.http import HttpResponse
from base.models import Customer

def homee(request):
    if request.session.get('custid'):
        custid=request.session.get('custid')
        user=Customer.objects.get(custid=custid)
        return render(request, "home.html",{'user':user})
    return render(request, "home.html")