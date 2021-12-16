
from django.urls import path

import adminapp.views as adminapp  # Здесь импортируем наш контроллер из views

app_name = 'adminapp' # Указываю, что этот файл работает в пространстве имен adminapp

urlpatterns = [
    path('', adminapp.index, name='index'),
]
