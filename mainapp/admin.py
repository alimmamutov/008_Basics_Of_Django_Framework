from django.contrib import admin
from .models import Product, ProductCategory

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(ProductCategory, 'name'))

    class Meta:
        model = Product


class ProductAdmin (ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = [field.name for field in Product._meta.fields if field.name != 'id']


# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
