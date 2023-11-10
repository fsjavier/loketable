from django.test import TestCase


class TestViews(TestCase):
    """
    Test home views
    """

    def test_get_home_page(self):
        """
        Test home page response
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
