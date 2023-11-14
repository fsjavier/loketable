from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Conversation
from products.models import Product
from profiles.models import Profile
from .forms import ConversationMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class StartConversation(LoginRequiredMixin, View):
    """
    Start a conversation
    """

    def get(self, request, product_id, slug):
        """
        If a conversation already exists for the product
        redirect the user to it.
        If not, render the form.
        """
        product = get_object_or_404(Product, id=product_id)

        # Redirect to products page if trying to access url to
        # start a conversation for own product
        if product.user == request.user:
            return redirect('products')

        conversations = Conversation.objects.filter(
            product=product
        ).filter(
            members__in=[request.user.id]
        )

        if conversations:
            return redirect(
                'conversation_messages', pk=conversations.first().id
            )

        form = ConversationMessageForm()
        context = {
            'form': form,
            'product': product
        }
        return render(
            request,
            'conversations/new_conversation.html',
            context
        )

    def post(self, request, product_id, slug):
        """
        Save the new conversation and message and
        redirect the user to the product details
        """

        product = get_object_or_404(Product, id=product_id)

        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(product=product)
            conversation.members.add(request.user)
            conversation.members.add(product.user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            messages.success(
                self.request,
                f'Your message to {product.user} was sent successfully'
            )

            return redirect(reverse('product_detail', args=[product_id, slug]))

        return render(
            request,
            'conversations/new_conversation.html',
            {'form': form}
        )


class InboxMessages(LoginRequiredMixin, generic.ListView):
    """
    View all conversations
    """

    model = Conversation
    template_name = 'conversations/inbox_conversations.html'
    context_object_name = 'conversations'
    paginate_by = 8

    def get_queryset(self, **kwargs):
        """
        Return user's conversations
        """
        conversations = self.model.objects.filter(
            members__in=[self.request.user.id]).order_by('-modified_date')

        return conversations


class ConversationMessages(LoginRequiredMixin, View):
    """
    View all messages for a conversation
    """

    def get(self, request, pk):
        """
        Get all messages and passed them together
        with the form. If the user tries to access a
        non-existing conversation redirect to Inbox
        """

        try:
            conversation = Conversation.objects.filter(
                members__in=[request.user.id]).get(pk=pk)
            form = ConversationMessageForm()
            context = {
                'conversation': conversation,
                'form': form
            }
            return render(
                request, 'conversations/conversation_messages.html', context
            )

        except Conversation.DoesNotExist:
            return redirect('inbox_conversations')

    def post(self, request, pk):
        """
        When a new message is sent keep the user
        in the conversation page
        """
        conversation = Conversation.objects.filter(
            members__in=[request.user.id]).get(pk=pk)
        form = ConversationMessageForm(request.POST)
        context = {
            'conversation': conversation,
            'form': form
        }

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation_messages', pk=pk)

        return render(
            request, 'conversations/conversation_messages.html', context
        )
