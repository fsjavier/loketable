from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    """
    Form to send a message
    """
    class Meta:
        model = Product
        fields = [
            'content',
        ]

        labels = {
            'content': 'Message',
        }
