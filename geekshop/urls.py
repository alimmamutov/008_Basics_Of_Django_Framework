"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # импортируем для настроек media
from django.conf.urls.static import static  # импортируем для настроек media

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),  # Здесь добавляю urls из mainapp
    path('auth/', include('authapp.urls', namespace='auth')),  # Здесь добавляю urls из authapp
    path('admin/', admin.site.urls, name='admin'),
    path('basket/', include('basketapp.urls', namespace='basket'))
]

# Сообщаю Django, что папка на диске MEDIA_ROOT доступна по сетевому адресу MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)