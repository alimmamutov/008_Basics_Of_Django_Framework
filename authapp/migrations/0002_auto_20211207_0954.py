# Generated by Django 2.2 on 2021-12-07 06:54

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, validators=[authapp.models.validate_date_of_birth], verbose_name='возраст'),
        ),
    ]
