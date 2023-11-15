from django.test import TestCase
from django.contrib.auth.models import User
from .models import Conversation, ConversationMessage
from products.models import Product


class TestViews(TestCase):
    """
    Test conversation views
    """

    def setUp(self):
        """
        Create a test users, product and conversation
        """
        self.user1 = User.objects.create_user(
            username='test_user1',
            password='test_password1'
        )

        self.user2 = User.objects.create_user(
            username='test_user2',
            password='test_password2'
        )

        self.product = Product.objects.create(
            user=self.user1,
            title='Test product',
            description='Test product description',
            country='Country',
            city='City',
            category='fruit',
            price=10.50,
            currency='eur',
            available=True,
            quantity=10,
            units='kg'
        )

        self.conversation = Conversation.objects.create(
            product=self.product,
        )

        self.conversation.members.set([self.user1, self.user2])

        self.message = ConversationMessage.objects.create(
            conversation=self.conversation,
            content='test message',
            created_by=self.user1
        )

    def test_get_inbox_page_logged_in_user(self):
        """
        Test inbox page response for a logged in user
        """
        self.client.login(username='test_user1', password='test_password1')
        response = self.client.get('/inbox/conversations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'conversations/inbox_conversations.html'
        )

    def test_get_inbox_page_logged_out_user(self):
        """
        Test logged out user is redirected when trying
        to access inbox page url
        """
        response = self.client.get('/inbox/conversations/')
        self.assertEqual(response.status_code, 302)

    def test_get_conversation_messages(self):
        """
        Test conversation messages page loads
        for existing conversation
        """
        self.client.login(username='test_user1', password='test_password1')
        response = self.client.get(
            f'/inbox/conversations/{self.conversation.id}/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'conversations/conversation_messages.html'
        )

    def test_get_conversation_messages_logged_out_user(self):
        """
        Test conversation messages page redirect
        a logged out user
        """
        response = self.client.get(
            f'/inbox/conversations/{self.conversation.id}/'
        )
        self.assertEqual(response.status_code, 302)

    def test_messages_are_loaded(self):
        """
        Test conversation messages are loaded
        in conversation messages page
        """
        self.client.login(username='test_user1', password='test_password1')
        response = self.client.get(
            f'/inbox/conversations/{self.conversation.id}/'
        )
        messages_count = ConversationMessage.objects.filter(
            conversation=self.conversation
        ).count()
        self.assertEqual(messages_count, 1)

    def test_get_new_conversation_from_contact_producer(self):
        """
        Test the New Conversation page is loaded
        when starting a new conversation
        """
        self.client.login(username='test_user1', password='test_password1')
        product2 = Product.objects.create(
            user=self.user2,
            title='Test product 2',
            description='Test product description 2 ',
            country='Country',
            city='City',
            category='fruit',
            price=10.50,
            currency='eur',
            available=True,
            quantity=10,
            units='kg'
        )
        response = self.client.get(
            f'/inbox/new/{product2.id}/{product2.slug}/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'conversations/new_conversation.html'
        )

    def test_user_redirected_from_contact_producer_existing_conversation(self):
        """
        Test the user is redirected if a conversation already exists
        """
        self.client.login(username='test_user2', password='test_password2')
        response = self.client.get(
            f'/inbox/new/{self.product.id}/{self.product.slug}/'
        )

    def test_user_can_not_start_conversation_own_product(self):
        """
        Test a user is redirected to products page if trying to start a
        conversation for a own product
        """
        self.client.login(username='test_user1', password='test_password1')
        response = self.client.get(
            f'/inbox/new/{self.product.id}/{self.product.slug}/'
        )
