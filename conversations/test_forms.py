from django.test import TestCase
from .forms import ConversationMessageForm


class TestConversationMessageForm(TestCase):
    """
    Test Conversation Message form
    """

    def test_content_is_required(self):
        """
        Test content is required
        """
        form = ConversationMessageForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(
            form.errors['content'][0], 'This field is required.'
        )
