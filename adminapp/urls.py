
from django.urls import path

import adminapp.views as adminapp  # Здесь импортируем наш контроллер из views

app_name = 'adminapp'  # Указываю, что этот файл работает в пространстве имен adminapp

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
]
