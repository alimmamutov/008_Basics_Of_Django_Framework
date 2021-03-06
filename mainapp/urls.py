
from django.urls import path, re_path

import mainapp.views as mainapp  # Здесь импортируем наш контроллер из views

app_name = 'mainapp' # Указываю, что этот файл работает в пространстве имен mainapp

urlpatterns = [
    path('', mainapp.index, name='index'),  # Назначаем домашней странице обработчик index из views
    path('<int:page>', mainapp.index, name='index_pagination'),  # Если выбрана определенная страница из домашней
    # path('cart/', mainapp.cart, name='cart'),
    path('checkout/', mainapp.checkout, name='checkout'),
    path('product-details/<int:product_id>', mainapp.product_details, name='product_details'),
    # path('shop/<int:category_id>', mainapp.shop, name='shop'),
    re_path(r'shop/(?P<category_id>\d+)/products', mainapp.shop, name='shop'),
    path('test_page/', mainapp.test_page, name='test_page'),
]

a = 0

