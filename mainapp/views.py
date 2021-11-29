from django.shortcuts import render
from .models import Product, ProductCategory  # импортирую модели для формирования списка товаров
import random

# Create your views here.
links_menu = [{'href': 'main:index', 'name': 'Home'},
              {'href': 'main:shop', 'name': 'Shop'},
              {'href': 'main:cart', 'name': 'Cart'},
              {'href': 'main:checkout', 'name': 'Checkout'},
              {'href': 'main:test_page', 'name': 'Test page'}
              ]


def index(request):

    content = {
        'title': 'Amado - Furniture Ecommerce | Home',
        'links_menu': links_menu,
        'product_list': sorted(Product.objects.all()[:], key=lambda x: random.random())
    }
    return render(request, 'mainapp/index.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def cart(request):
    content = {
        'title': 'Amado - Furniture Ecommerce | Cart',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/cart.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def shop(request, category_id=None):
    content = {
        'title': 'Amado - Furniture Ecommerce | Shop',
        'links_menu': links_menu,
        'category_id': category_id,
        'product_list': Product.objects.filter(category_id=category_id),
        'category_list': ProductCategory.objects.all()  # // Получил список всех категорий
    }
    return render(request, 'mainapp/shop.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def checkout(request):
    content = {
        'title': 'Amado - Furniture Ecommerce | Checkout',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/checkout.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def product_details(request, product_id=None):
    content = {
        'title': 'Amado - Furniture Ecommerce | Product details',
        'links_menu': links_menu,
        'product_id': product_id,
        'product_item': Product.objects.filter(id=product_id)
    }
    return render(request, 'mainapp/product-details.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def test_page(request):
    products_list = [
        {'price': '150', 'img': '/static/img/bg-img/1.jpg', 'name': 'Modern Chair'},
        {'price': '250', 'img': '/static/img/bg-img/2.jpg', 'name': 'Minimalistic Plant Pot'},
        {'price': '300', 'img': '/static/img/bg-img/3.jpg', 'name': 'Modern Chair'},
        {'price': '350', 'img': '/static/img/bg-img/4.jpg', 'name': 'Night Stand'},
        {'price': '400', 'img': '/static/img/bg-img/5.jpg', 'name': 'Plant Pot'},
        {'price': '450', 'img': '/static/img/bg-img/6.jpg', 'name': 'Small Table'},
        {'price': '500', 'img': '/static/img/bg-img/7.jpg', 'name': 'Metallic Chair'},
        {'price': '550', 'img': '/static/img/bg-img/8.jpg', 'name': 'Modern Rocking Chair'},
        {'price': '600', 'img': '/static/img/bg-img/9.jpg', 'name': 'Home Deco'}
    ]
    content_test = {
        'title': 'тестовая страница',
        'links_menu': links_menu,
        'products_list': products_list
    }
    return render(request, 'mainapp/test_page.html', context=content_test)
