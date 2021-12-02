import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):  # Процедура загрузки из файла json
    with open(os.path.join(settings.JSON_PATH, file_name + '.json'), 'r') as file:  # Открываем файл и даем ему имя file
        return json.load(file)  # Возвращаем словарь из json файла


class Command(BaseCommand):  # Обязательный класс, который должен находиться в команде для отображения в manage.py
    help = 'Загрузка категорий и продуктов из JSON'

    def handle(self, *args, **options):  # Обязательная процедура - основной алгоритм команды
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for prod in products:
            category_name = prod['category']
            _category = ProductCategory.objects.get(name=category_name)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser(username='django', email='admin@geekshop.local', password='geekbrains')