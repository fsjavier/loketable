from django.test import TestCase
from .forms import ProfileForm


class TestProfileForm(TestCase):
    """
    Test profile form
    """

    def test_all_fields_are_optional(self):
        """
        Test all fields can be empty
        """
        form = ProfileForm({
            'first_name': '',
            'last_name': '',
            'bio': '',
            'country': '',
            'city': '',
            'contact': ''
        })
        self.assertTrue(form.is_valid())
