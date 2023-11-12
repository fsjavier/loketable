from django.urls import path
from .views import StartConversation, InboxMessages, ConversationMessages

urlpatterns = [
    path(
        'new/<int:product_id>/<slug:slug>/',
        StartConversation.as_view(),
        name='start_conversation'
    ),
    path(
        'conversations/',
        InboxMessages.as_view(),
        name='inbox_conversations'
    ),
    path(
        'conversations/<int:pk>',
        ConversationMessages.as_view(),
        name='conversation_messages'
    ),
]
