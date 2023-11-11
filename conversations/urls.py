from django.urls import path
from .views import StartConversation

urlpatterns = [
    path('new/<int:product_id>/', StartConversation.as_view(), name='start_conversation'),
]
