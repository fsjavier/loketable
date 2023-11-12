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
    Start a conversation or go to the conversation
    if already exists
    """

    def get(self, request, product_id, slug):

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
            return redirect('products')

        form = ConversationMessageForm()
        return render(
            request,
            'conversations/new_conversation.html',
            {'form': form}
        )

    def post(self, request, product_id, slug):

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
