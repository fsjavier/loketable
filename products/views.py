from django.shortcuts import (
    redirect,
    get_object_or_404,
    HttpResponseRedirect,
    reverse
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic, View
from django.db.models import Q
from .models import Product, CATEGORIES
from profiles.models import Favorite

from .forms import ProductForm


class ProductsList(generic.ListView):
    """
    View all products
    """
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self, **kwargs):
        """
        Return filtered products
        """
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')

        products = self.model.objects.filter(
            available=True).order_by('-updated_date')

        if query:
            products = products.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__icontains=query)
            )

        if category:
            products = products.filter(category=category)

        return products

    def get_context_data(self, **kwargs):
        """
        Provide context to use in the template
        """
        context = super().get_context_data(**kwargs)

        # Check if there is a query and assign it to the context
        if self.request.GET.get('q'):
            context['query'] = self.request.GET.get('q')

        # Check if there is a category and if there is
        # assign the readable value to the context
        if self.request.GET.get('category'):
            category = self.request.GET.get('category')
            for cat in CATEGORIES:
                if cat[0] == category:
                    context['category'] = cat[1]
                    break

        context['categories'] = CATEGORIES

        products = context['products']

        # Checking for authentication is needed here
        # Otherwise Django will throw an error because
        # Anonymous users can't have favorites
        if self.request.user.is_authenticated:

            # Get a list of favorited product IDs for the current user
            # https://stackoverflow.com/questions/37205793/django-values-list-vs-values
            favorite_product_ids = self.request.user.favorited.values_list(
                'product',
                flat=True
                )

            # For each product, check if it's in the list of favorites
            for product in products:
                product.is_favorite = product.id in favorite_product_ids

        return context


class AddProduct(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.CreateView
):
    """
    Add a product
    """
    template_name = 'products/add_product.html'
    model = Product
    form_class = ProductForm
    success_message = '%(title)s added successfully'

    def get_success_url(self):
        """
        Return to user's profile
        """
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        """
        Assign the form instance to the user making the request
        """
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)

    def test_func(self):
        """
        Requires the user to be the owner of the object
        """
        return self.request.user.is_authenticated


class EditProduct(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    """
    Edit a Product
    """
    template_name = 'products/add_product.html'
    form_class = ProductForm
    model = Product
    success_message = '%(title)s edited successfully'

    def get_success_url(self):
        """
        Return to user's profile
        """
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        """
        Assign the form instance to the user making the request
        """
        form.instance.user = self.request.user
        return super(EditProduct, self).form_valid(form)

    def test_func(self):
        """
        Requires the user to be the owner of the object
        """
        return self.request.user == self.get_object().user


class ToggleProduct(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    """
    Toggle a Product
    """
    model = Product
    fields = ['available']

    def get_success_url(self):
        """
        Return to user's profile
        """
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        """
        Assign the form instance to the user making the request
        Assign the product the new availability
        Add a message depending if the product has been enabled or disabled
        """
        form.instance.user = self.request.user
        form.instance.available = form.instance.available
        form.save()
        if form.instance.available:
            messages.success(
                self.request, f'{form.instance.title} enabled successfully'
            )
        else:
            messages.success(
                self.request, f'{form.instance.title} disabled successfully'
            )
        return super(ToggleProduct, self).form_valid(form)

    def test_func(self):
        """
        Requires the user to be the owner of the object
        """
        return self.request.user == self.get_object().user


class DeleteProduct(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
):
    """
    Delete a product
    """
    model = Product
    success_message = "%(title)s deleted successfully"

    def get_success_message(self, cleaned_data):
        """
        Get data from the object to use in the success message
        """
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

    def get_success_url(self):
        """
        Return to user's profile
        """
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def test_func(self):
        """
        Requires the user to be the owner of the object
        """
        return self.request.user == self.get_object().user


class ProductDetail(generic.DetailView):
    """
    View product details
    """
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'


class ProductListAddFavorite(View):
    """
    Add or remove a product from your favorites
    """
    def post(self, request, slug, product_id):
        product = get_object_or_404(Product, id=product_id, slug=slug)

        if product.favorited_by.filter(id=request.user.id).exists():
            product.favorited_by.remove(request.user)
            # Get the instance from the Favorites if it exists
            # Or create one if it doesn't
            # https://www.letscodemore.com/blog/django-get-or-create/
            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                product=product
                )
            favorite.delete()
            messages.warning(
                request, f'{product.title} removed from favorites'
            )
        else:
            product.favorited_by.add(request.user)
            # Get the instance from the Favorites if it exists
            # Or create one if it doesn't
            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                product=product
                )
            messages.warning(
                request, f'{product.title} added to favorites'
                )

        return redirect('products')


class FavoriteProductsList(LoginRequiredMixin, generic.ListView):
    """
    View all products
    """
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 8
    success_url = '/favorites/'

    def get_queryset(self, **kwargs):
        """
        Return filtered products
        """
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')

        products = self.model.objects.all().order_by('-updated_date')
        favorite_product_ids = self.request.user.favorited.values_list(
            'product',
            flat=True
            )
        products = products.filter(id__in=favorite_product_ids)

        if query:
            products = products.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__icontains=query)
            )

        if category:
            products = products.filter(category=category)

        return products

    def get_context_data(self, **kwargs):
        """
        Provide context to use in the template
        """
        context = super().get_context_data(**kwargs)

        # Check if there is a query and assign it to the context
        if self.request.GET.get('q'):
            context['query'] = self.request.GET.get('q')

        # Check if there is a category and if there is
        # assign the readable value to the context
        if self.request.GET.get('category'):
            category = self.request.GET.get('category')
            for cat in CATEGORIES:
                if cat[0] == category:
                    context['category'] = cat[1]
                    break

        context['categories'] = CATEGORIES

        products = context['products']

        # Checking for authentication is needed here
        # Otherwise Django will throw an error because
        # Anonymous users can't have favorites
        if self.request.user.is_authenticated:

            # Get a list of favorited product IDs for the current user
            # https://stackoverflow.com/questions/37205793/django-values-list-vs-values
            favorite_product_ids = self.request.user.favorited.values_list(
                'product',
                flat=True
                )

            # For each product, check if it's in the list of favorites
            for product in products:
                product.is_favorite = product.id in favorite_product_ids

        return context
