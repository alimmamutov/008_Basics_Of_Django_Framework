from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.


def validate_date_of_birth(age):  # "это функция для собственного валидатора
    if age < 18:
        raise ValidationError('Вы слишком молоды!')


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True, validators=[validate_date_of_birth])
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
