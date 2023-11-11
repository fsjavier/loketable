from django.contrib import admin
from .models import Conversation, ConversationMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """
    Class to display conversations on admin
    """

    list_display = (
        'product',
        'created_date',
        'modified_date',
    )
    list_filter = (
        'product',
        'members',
        'created_date'
    )
    search_fields = (
        'product',
        'members'
    )


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    """
    Class to display convesation messages on admin
    """

    list_display = (
        'conversation',
        'created_by',
        'created_date'
    )

    list_filter = (
        'conversation',
        'created_by',
        'created_date'
    )

    search_fields = (
        'conversation',
        'created_by'
    )
