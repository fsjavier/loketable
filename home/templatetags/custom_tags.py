# Idea to create custom filters from:
# https://realpython.com/django-template-custom-tags-filters/#writing-django-template-custom-filters

from django import template

register = template.Library()


@register.filter
def search_bar_urls(url_name):
    """
    Filter that receives a url name and checks if it's not
    one of the urls that should include the search bar.
    """
    included_urls = [
        'home',
        'products',
        'favorites'
    ]

    return url_name not in included_urls
