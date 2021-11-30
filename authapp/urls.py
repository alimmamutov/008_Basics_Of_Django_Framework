
from django.urls import path

import authapp.views as authapp  # Здесь импортируем наш контроллер из views

app_name = 'authapp' # Указываю, что этот файл работает в пространстве имен authapp

urlpatterns = [
    # path('', auth.index, name='index'),  # Назначаем домашней странице обработчик index из views
]
