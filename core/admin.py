from django.contrib import admin
from core.models import *

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'product_name', 'product_description', 'image', 'product_quantity', 'product_price', 'product_id']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(SupportCase)
admin.site.register(Promotion)
admin.site.register(Invoice)