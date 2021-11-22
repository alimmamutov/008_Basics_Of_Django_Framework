from django.shortcuts import render

# Create your views here.
links_menu = [{'href': 'index', 'name': 'Home'},
              {'href': 'shop', 'name': 'Shop'},
              {'href': 'product_details', 'name': 'Product'},
              {'href': 'cart', 'name': 'Cart'},
              {'href': 'checkout', 'name': 'Checkout'},
              {'href': 'test_page', 'name': 'Test page'}
              ]
content = {
    'title': 'тестовая страница',
    'links_menu': links_menu
}


def index(request):
    return render(request, 'mainapp/index.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def cart(request):
    return render(request, 'mainapp/cart.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def shop(request):
    return render(request, 'mainapp/shop.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def checkout(request):
    return render(request, 'mainapp/checkout.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates


def product_details(request):
    return render(request, 'mainapp/product-details.html',
                  context=content)  # Второй параметр - это путь html страницы, относительно templates

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

content = {
    'title': 'тестовая страница',
    'links_menu': links_menu,
    'products_list': products_list
}


def test_page(request):
    return render(request, 'mainapp/test_page.html', context=content)
