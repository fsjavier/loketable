from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
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
