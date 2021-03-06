from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, AdminProductCategoryUpdateForm, \
    AdminProductUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# @user_passes_test(lambda x: x.is_superuser)  # Этот декоратор пропустит в админку только юзера, удовл условиям в скобках
# def index(request):
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': 'админка/пользователи',
#         'object_list': users_list
#     }
#
#     return render(request, 'adminapp/index.html', context)


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context


class ShopUserList(SuperUserOnlyMixin, PageTitleMixin, ListView):  # это заменяет контроллер индексной страницы админки
    model = ShopUser
    page_title = 'Все пользователи / Список'
    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, request, *args, **kwargs):  # Данная функция не разрешает открывать шаблон незалогиненным пользователям
    #     return super().dispatch(request, *args, **kwargs)


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


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     if request.method == 'POST':
#         form = AdminProductCategoryUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('my_admin:categories'))
#     else:
#         form = AdminProductCategoryUpdateForm()
#
#     context = {
#         'title': 'категории продуктов/создание',
#         'form': form
#     }
#     return render(request, 'adminapp/category_update.html', context)


class ProductCategoryCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    success_url = reverse_lazy('my_admin:categories')  # После успешного создания, перенаправит на указанную страницу
    page_title = 'Категории продуктов / Создание'

    # fields = '__all__' # Это стандартное назначение всех полей формы
    form_class = AdminProductCategoryUpdateForm  # Если отключили стандартное включения полей формы
    # то используем готовую форму из файла forms


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     obj = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         form = AdminProductCategoryUpdateForm(request.POST, request.FILES, instance=obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('my_admin:categories'))
#     else:
#         form = AdminProductCategoryUpdateForm(instance=obj)
#
#     context = {
#         'title': 'категории продуктов/редактирование',
#         'form': form
#     }
#     return render(request, 'adminapp/category_update.html', context)


class ProductCategoryUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('my_admin:categories')  # После успешного создания, перенаправит на указанную страницу
    form_class = AdminProductCategoryUpdateForm
    page_title = 'Категории продуктов / Редактирование'

    # def get_context_data(self, **kwargs): #  заменил на наследовани из миксина
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Категории продуктов/редактирование'
    #     return context


# @user_passes_test(lambda x: x.is_superuser)
# def category_delete(request, pk):
#     obj = get_object_or_404(ProductCategory, pk=pk)
#     # user.delete()  # not good
#
#     if request.method == 'POST':
#         obj.is_active = not obj.is_active
#         obj.save()
#         return HttpResponseRedirect(reverse('my_admin:categories'))
#
#     context = {
#         'title': 'категори/удаление',
#         'object': obj,
#     }
#     return render(request, 'adminapp/category_delete.html', context)


class ProductCategoryDelete(SuperUserOnlyMixin, DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('my_admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, category_pk):
    category = get_object_or_404(ProductCategory, pk=category_pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'my_admin:category_products',
                kwargs={'pk': category.pk}
            ))
    else:
        form = AdminProductUpdateForm(
            initial={  # в данный аргумент добавляем словарь с инициализацией реквизитов модели
                'category': category,
                # 'quantity': 10,
                # 'price': 157.9,
            }
        )

    context = {
        'title': 'продукты/создание',
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'my_admin:category_products',
                kwargs={'pk': product.category.pk}
            ))
    else:
        form = AdminProductUpdateForm(instance=product)

    context = {
        'title': 'продукты/редактирование',
        'form': form,
        'category': product.category,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.is_active = False
        obj.save()
        return HttpResponseRedirect(reverse(
            'my_admin:category_products',
            kwargs={'pk': obj.category.pk}
        ))

    context = {
        'title': 'продукты/удаление',
        'object': obj,
    }
    return render(request, 'adminapp/product_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    context = {
        'title': 'продукты/подробнее',
        'object': obj,
    }
    return render(request, 'adminapp/product_read.html', context)


class ProductDetail(SuperUserOnlyMixin, PageTitleMixin, DetailView):
    model = Product
    page_title = 'Карточка продукта'
#     pk_url_kwarg = 'product_pk'
