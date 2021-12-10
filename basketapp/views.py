from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import links_menu


@login_required
def basket(request):
    content = {
        'links_menu': links_menu,
        'basket': Basket.objects.filter(user=request.user)
    }
    return render(request, 'basketapp/view.html', content)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:product_details', args=[pk]))
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)