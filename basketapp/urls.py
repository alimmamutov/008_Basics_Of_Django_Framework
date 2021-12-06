
from django.urls import path

import basketapp.views as basketapp  # Здесь импортируем наш контроллер из views

app_name = 'basketapp' # Указываю, что этот файл работает в пространстве имен authapp

urlpatterns = [
    path('', basketapp.basket, name='basket'),
]
