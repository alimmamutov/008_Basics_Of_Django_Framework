
from django.urls import path

import basketapp.views as basketapp  # Здесь импортируем наш контроллер из views

app_name = 'basketapp' # Указываю, что этот файл работает в пространстве имен authapp

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')
]
