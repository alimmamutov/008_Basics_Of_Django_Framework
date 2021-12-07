# Generated by Django 2.2 on 2021-12-07 06:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(code='invalid', inverse_match=False, message='В названии могут присутствовать только латинские буквы, цифры и пробелы', regex='^[A-Za-z0-9 ]+$')], verbose_name='имя продукта'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', inverse_match=False, message='В названии могут присутствовать только латинские буквы, цифры и пробелы', regex='^[A-Za-z0-9 ]+$')], verbose_name='имя'),
        ),
    ]