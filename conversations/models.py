from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Conversation(models.Model):
    """
    Model for conversations
    """
    product = models.ForeignKey(
        Product, related_name='conversations', on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    def __str__(self):
        return self.product


class ConversationMessage(models.Model):
    """
    Model for conversation messages
    """
    conversation = models.ForeignKey(
        Conversation, related_name='messages', on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='created_messages', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.conversation
