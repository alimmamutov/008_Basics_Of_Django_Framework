from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')  #Второй параметр - это путь html страницы, относительно templates


def cart(request):
    return render(request, 'mainapp/cart.html')  #Второй параметр - это путь html страницы, относительно templates


def shop(request):
    return render(request, 'mainapp/shop.html')  #Второй параметр - это путь html страницы, относительно templates


def checkout(request):
    return render(request, 'mainapp/checkout.html')  #Второй параметр - это путь html страницы, относительно templates


def product_details(request):
    return render(request, 'mainapp/product-details.html')  #Второй параметр - это путь html страницы, относительно templates