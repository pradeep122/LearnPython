from django.contrib import admin
from .models import Product, Offer

# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_dislay = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_dislay = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
