
from django.urls import path

import adminapp.views as adminapp  # Здесь импортируем наш контроллер из views

app_name = 'adminapp'  # Указываю, что этот файл работает в пространстве имен adminapp

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('user/delete_direct/<int:pk>/', adminapp.user_delete_direct, name='user_delete_direct'),
    path('category/list/', adminapp.categories, name='categories'),
    path('category/create/', adminapp.category_create, name='category_create'),
    path('category/update/<int:pk>', adminapp.category_update, name='category_update'),
]
