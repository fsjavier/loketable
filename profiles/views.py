from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile, Favorite
from products.models import Product
from .forms import ProfileForm


class Profiles(generic.DetailView):
    """ View User Profile """
    template_name = 'profiles/profile.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Checking for authentication is needed here
        # Otherwise Django will throw an error when
        # Anonymous users try to access a profile
        if self.request.user.is_authenticated:
            context['user_favorites'] = Favorite.objects.filter(
                user=self.request.user
                ).count()

        # Filter the products for the user
        user_products = Product.objects.filter(user=context['profile'].user)
        # Check if there's at least one un/available product
        context['is_any_product_available'] = user_products.filter(
            available=True).exists()
        context['is_any_product_unavailable'] = user_products.filter(
            available=False).exists()
        # Separate available and unavailable products
        available_products = user_products.filter(available=True)
        unavailable_products = user_products.filter(available=False)
        context['available_products'] = available_products
        context['unavailable_products'] = unavailable_products

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """ Edit a Profile """
    template_name = 'profiles/edit_profile.html'
    form_class = ProfileForm
    model = Profile

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditProfile, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
