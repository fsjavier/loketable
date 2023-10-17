from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
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
