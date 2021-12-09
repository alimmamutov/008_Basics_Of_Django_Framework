from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

onlyLatin = RegexValidator(
            regex=r'^[A-Za-z0-9 ]+$',
            message='В названии могут присутствовать только латинские буквы, цифры и пробелы',
            code='invalid',
            inverse_match=False
        )


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True, validators=[  # Добавил валидатор на латиницу
        onlyLatin
    ])
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128, validators=[onlyLatin])
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(max_length=60, verbose_name='краткое описание продукта', blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    def __str__(self):  # Представление объекта
        return f'{self.name} - {self.price}$ ({self.category.name})'
