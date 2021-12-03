from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render

from .forms import *
from .models import Product, ProductCategory  # импортирую модели для формирования списка товаров
import random

# Create your views here.
links_menu = [{'href': 'main:index', 'name': 'Home'},
              {'href': 'main:shop', 'name': 'Shop'},
              {'href': 'main:cart', 'name': 'Cart'},
              {'href': 'main:checkout', 'name': 'Checkout'},
              {'href': 'main:test_page', 'name': "Offer client's product"}
              ]


def index(request):

    content = {
        'title': 'Amado - Furniture Ecommerce | Home',
        'links_menu': links_menu,
        'product_list': sorted(Product.objects.all()[:], key=lambda x: random.random()),
        'page': request.GET.get("page", '1')
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
    form = ClientProductOffer()
    content_test = {
        'title': 'Предложить товар',
        'links_menu': links_menu,
        'form': form
    }
    return render(request, 'mainapp/test_page.html', context=content_test)
