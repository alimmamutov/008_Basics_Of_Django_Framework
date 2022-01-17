from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .forms import *
from .models import Product, ProductCategory  # импортирую модели для формирования списка товаров
import random


links_menu = [{'href': 'main:index', 'name': 'Home'},
              {'href': 'main:shop', 'name': 'Shop'},
              {'href': 'basket:view', 'name': 'Cart'},
              {'href': 'main:checkout', 'name': 'Checkout'},
              {'href': 'main:test_page', 'name': "Offer client's product"},
              # {'href': 'basket:view', 'name': "Basket"}
              ]


# Create your views here.
def get_basket(request):
    return request.user.is_authenticated and request.user.basket.all() or []


def index(request):

    content = {
        'title': 'Amado - Furniture Ecommerce | Home',
        'links_menu': links_menu,
        'product_list': sorted(Product.objects.all()[:], key=lambda x: random.random()),
        'page': request.GET.get("page", '1'),
        'basket': get_basket(request)
    }
    return render(request, 'mainapp/index.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


# def cart(request):
#     content = {
#         'title': 'Amado - Furniture Ecommerce | Cart',
#         'links_menu': links_menu,
#         'basket': initial_my_basket(request)
#     }
#     return render(request, 'mainapp/cart.html',
#                   context=content)  # Второй параметр - это путь html страницы, относительно templates


def shop(request, category_id=None, product_id=None):

    content = {
        'title': 'Amado - Furniture Ecommerce | Shop',
        'links_menu': links_menu,
        'category_id': int(category_id),
        'product_list': Product.objects.filter(category_id=category_id).order_by('-price'),  # сортировка по убыв (перед назв колонки поставить "-")
        # 'product_list': Product.objects.filter(category_id=category_id).order_by('price'),  # сортировка по возр
        'category_list': ProductCategory.objects.filter(is_active = True),  # // Получил список всех категорий
        'basket': get_basket(request)
    }
    """
       Вариант отбора списка продуктов по категории №2:
           cat = get_object_or_404(ProductCategory, pk=category_id)
           product_list = cat.product_set.all();
    """
    return render(request, 'mainapp/shop.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def checkout(request):
    content = {
        'title': 'Amado - Furniture Ecommerce | Checkout',
        'links_menu': links_menu,
        'basket': get_basket(request)
    }
    return render(request, 'mainapp/checkout.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def product_details(request, product_id=None):
    content = {
        'title': 'Amado - Furniture Ecommerce | Product details',
        'links_menu': links_menu,
        'product_id': product_id,
        'product_item': Product.objects.filter(id=product_id),
        'basket': get_basket(request)
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
