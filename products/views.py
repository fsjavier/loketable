from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Product, CATEGORIES
from profiles.models import Favorite
from .forms import ProductForm


class ProductsList(generic.ListView):
    """ View all products """
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6

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
    """ Add a product """
    template_name = 'products/add_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/products'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)


class ProductDetail(generic.DetailView):
    """ View product details """
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'
