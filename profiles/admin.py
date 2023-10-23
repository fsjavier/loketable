from django.contrib import admin
from .models import Profile, Favorite


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'country',
        'city',
    )
    list_filter = (
        'user',
        'country',
        'created_date'
    )
    search_fields = (
        'user',
        'title'
    )


@admin.register(Favorite)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product',
    )

    search_fields = (
        'user',
        'product'
    )
