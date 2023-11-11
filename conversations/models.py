from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Conversation(models.Model):
    """
    Model for conversations
    """
    product = models.ForeignKey(
        Product, related_name='conversation_product', on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name='conversation_member')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_date',)

    def __str__(self):
        return self.product.title


class ConversationMessage(models.Model):
    """
    Model for conversation messages
    """
    conversation = models.ForeignKey(
        Conversation, related_name='messages', on_delete=models.CASCADE
    )
    content = models.TextField(max_length=1000, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='message_user', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.conversation.product.title
