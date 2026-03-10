from django.contrib import admin

# Register your models here.
from django.shortcuts import render

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html')