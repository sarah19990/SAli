from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'electronic_products/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'electronic_products/about.html',  {'title': 'About Us'})

def contact(request):
    return render(request, 'electronic_products/contact.html',  {'title': 'Contact Us'})

def product(request):
    return render(request, 'electronic_products/product.html',  {'title': 'Product'})