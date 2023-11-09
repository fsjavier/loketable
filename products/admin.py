from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Class to display products on admin
    """

    list_display = (
        'id',
        'user',
        'title',
        'category',
        'price',
        'currency',
        'available',
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
