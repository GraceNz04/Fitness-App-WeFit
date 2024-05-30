from django.http import HttpResponse
from django.shortcuts import render

from .models import User, Exercise

def registration(request): 
    return render(request, "registration.html")

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")