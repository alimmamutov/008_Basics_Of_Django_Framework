from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, AdminProductCategoryUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda x: x.is_superuser)  # Этот декоратор пропустит в админку только юзера, удовл условиям в скобках
def index(request):

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': 'админка/пользователи',
        'object_list': users_list
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):

    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'title': 'пользователи/создание',
        'update_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'title': 'пользователи/редактирование',
        'update_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    # user.delete()  # not good

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:index'))

    context = {
        'title': 'пользователи/удаление',
        'user_to_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete_direct(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    # user.delete()  # not good

    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('my_admin:index'))

    context = {
        'title': 'пользователи/удаление',
        'user_to_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    categories = ProductCategory.objects.all()
    context = {
        'title': 'administration/categories',
        'object_list': categories,
    }
    return render(request, 'adminapp/categories_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        form = AdminProductCategoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_admin:categories'))
    else:
        form = AdminProductCategoryUpdateForm()

    context = {
        'title': 'категории продуктов/создание',
        'form': form
    }
    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = AdminProductCategoryUpdateForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_admin:categories'))
    else:
        form = AdminProductCategoryUpdateForm(instance=obj)

    context = {
        'title': 'категории продуктов/редактирование',
        'form': form
    }
    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def category_delete(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    # user.delete()  # not good

    if request.method == 'POST':
        obj.is_active = not obj.is_active
        obj.save()
        return HttpResponseRedirect(reverse('my_admin:categories'))

    context = {
        'title': 'категори/удаление',
        'object': obj,
    }
    return render(request, 'adminapp/category_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all()
    context = {
        'title': f'категория {category.name}/продукты',
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/category_products_list.html', context)
