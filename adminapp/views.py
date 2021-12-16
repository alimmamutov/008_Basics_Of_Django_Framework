from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.
from authapp.models import ShopUser


@user_passes_test(lambda x: x.is_superuser) #  Этот декоратор пропустит в админку только юзера, удовл условиям в скобках
def index(request):

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': 'админка/пользователи',
        'object_list': users_list
    }

    return render(request, 'adminapp/index.html', context)
