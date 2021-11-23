
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp  # Здесь импортируем наш контроллер из views

app_name = 'mainapp' # Указываю, что этот файл работает в пространстве имен mainapp

urlpatterns = [
    path('', mainapp.index, name='index'),  # Назначаем домашней странице обработчик index из views
    path('cart/', mainapp.cart, name='cart'),
    path('checkout/', mainapp.checkout, name='checkout'),
    path('product-details/', mainapp.product_details, name='product_details'),
    path('shop/', mainapp.shop, name='shop'),
    path('test_page/', mainapp.test_page, name='test_page'),
]
