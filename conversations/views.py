from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Conversation
from products.models import Product
from .forms import ConversationMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StartConversation(View):

    def get(self, request, product_id):
        
        product = get_object_or_404(Product, id=product_id)
        
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


    def post(self, request, product_id):

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

            return redirect('products')
        return render(
            request,
            'conversations/new_conversation.html',
            {'form': form}
        )
