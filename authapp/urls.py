
from django.urls import path

import authapp.views as authapp  # Здесь импортируем наш контроллер из views

app_name = 'authapp' # Указываю, что этот файл работает в пространстве имен authapp

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
]
