from django.shortcuts import render
from django.http import HttpResponse

def homee(request):
    return render(request, "home.html")