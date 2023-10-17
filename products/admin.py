from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'title',
        'category',
        'price',
        'currency'
    )
    list_filter = (
        'user',
        'category',
        'created_date'
    )
    search_fields = (
        'user',
        'title'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
