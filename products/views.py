from django.shortcuts import (
    redirect,
    get_object_or_404,
    HttpResponseRedirect,
    reverse
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
        context = super().get_context_data(**kwargs)
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


class AddProduct(generic.CreateView):
    """
    Add a product
    """
    template_name = 'products/add_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)


class EditProduct(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """ Edit a Product """
    template_name = 'products/add_product.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditProduct, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class ToggleProduct(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    """ Toggle a Product """
    model = Product
    fields = ['available']

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.available = form.instance.available
        form.save()
        return super(ToggleProduct, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteProduct(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
):
    model = Product

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def test_func(self):
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
        else:
            product.favorited_by.add(request.user)
            # Get the instance from the Favorites if it exists
            # Or create one if it doesn't
            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                product=product
                )

        return redirect('products')


class FavoriteProductsList(generic.ListView):
    """
    View all products
    """
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 8
    success_url = '/favorites/'

    def get_queryset(self, **kwargs):
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
        context = super().get_context_data(**kwargs)
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
