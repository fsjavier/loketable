from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    """
    Form to send a message
    """
    class Meta:
        model = ConversationMessage
        fields = [
            'content',
        ]

        labels = {
            'content': 'Message',
        }
