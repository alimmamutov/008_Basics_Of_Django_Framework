from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(verbose_name='add time', auto_now_add=True)

    @property
    def item_sum(self):
        _sum = self.product.price * self.quantity
        return _sum

    @property
    def total(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = len(set(map(lambda x: x.product, _items)))
        _total_cost = sum(list(map(lambda x: x.item_sum, _items)))
        a = self.item_sum
        return {
            "total_quantity": _total_quantity,
            "total_cost": _total_cost
        }
