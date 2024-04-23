from django.contrib import admin
from .models import Product, Order, User


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity"]
    ordering = ["name", "-quantity"]
    list_filter = ["date_add", "price"]
    search_fields = ["description"]
    search_help_text = "Поиск по полю Описание продукта(description)"
    actions = [reset_quantity]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(User)
