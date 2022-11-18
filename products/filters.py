from django_filters import rest_framework as filters
from .models import Item


class ItemFilter(filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'category__title': ['exact'],
            'tags__title': ['exact'],
            'price': ['lt', 'gt'],
        }
