from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, "todos/login.html")

def register(request):
    return render(request, "todos/register.html")


def product_register(request):
    return render(request, "todos/product-register.html")

def product_edit(request):
    return render(request, "todos/product-edit.html")

def product_list(request):
    return render(request, "todos/product-list.html")