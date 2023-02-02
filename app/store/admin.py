from django.contrib import admin
from .models import Cart, Category, Product, CartItem

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class CartItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
