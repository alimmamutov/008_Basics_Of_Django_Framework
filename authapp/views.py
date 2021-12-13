from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.models import ShopUser

# Create your views here.
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserCreateForm, ShopUserUpdateForm


def login(request):

    # При переходе на страницу логина, когда срабатывает декоратор @login_required, в GET-переменной next передается
    # исходный адрес. Если хотели добавить в корзину товар с pk=3, в адресной строке браузера увидим:
    # http://127.0.0.1:8000/auth/login/?next=/basket/add/3/

    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # return HttpResponseRedirect('/')
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main'))
    else:
        form = ShopUserLoginForm()
    context = {
        'title': 'Вход в систему',
        'form': form,
        'next': next
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def create_new_user(request):
    ShopUser.objects.create_user(username=request.POST['username'],
                                 email=request.POST['email'],
                                 password=request.POST['password1'],
                                 avatar=request.POST['avatar'],
                                 first_name=request.POST['first_name'],
                                 last_name=request.POST['last_name'],
                                 is_active=True
                                 )


def registration(request):
    if request.method == 'POST':
        form = ShopUserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            create_new_user(request)
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))

    else:
        form = ShopUserCreateForm()
    context = {
        'title': 'Регистрация в системе',
        'form': form
    }
    return render(request, 'authapp/registration.html', context)


def update(request):
    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES,
                                  instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = ShopUserUpdateForm(instance=request.user)
    context = {
        'title': 'профиль пользователя',
        'form': form,
    }
    return render(request, 'authapp/update.html', context)