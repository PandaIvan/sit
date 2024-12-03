from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Promotion

admin.sites.AdminSite.site_header = "Админ-панель"
admin.sites.AdminSite.index_title = "Приложения"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    class Media:
        css = {
            'all': ('admin/admin_custom.css',)
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

    class Media:
        css = {
            'all': ('admin/admin_custom.css',)
        }


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

    class Media:
        css = {
            'all': ('admin/admin_custom.css',)
        }


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

    class Media:
        css = {
            'all': ('admin/admin_custom.css',)
        }


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)
    list_filter = ('active',)
