from django.shortcuts import render

# Create your views here.
links_menu = [{'href': 'index', 'name': 'Home'},
              {'href': 'shop', 'name': 'Shop'},
              {'href': 'product_details', 'name': 'Product'},
              {'href': 'cart', 'name': 'Cart'},
              {'href': 'checkout', 'name': 'Checkout'}
            ]
content = {
    'title': 'тестовая страница',
    'links_menu': links_menu
}


def index(request):
    return render(request, 'mainapp/index.html', context=content)  #Второй параметр - это путь html страницы, относительно templates


def cart(request):
    return render(request, 'mainapp/cart.html', context=content)  #Второй параметр - это путь html страницы, относительно templates


def shop(request):
    return render(request, 'mainapp/shop.html', context=content)  #Второй параметр - это путь html страницы, относительно templates


def checkout(request):
    return render(request, 'mainapp/checkout.html', context=content)  #Второй параметр - это путь html страницы, относительно templates


def product_details(request):
    return render(request, 'mainapp/product-details.html', context=content)  #Второй параметр - это путь html страницы, относительно templates


def test_page(request):
    return render(request, 'mainapp/test_page.html', context=content)

