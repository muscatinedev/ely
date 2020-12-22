import django_filters
from django_filters import CharFilter, DateFilter
from .models import Recipe


class RecipeFilter(django_filters.FilterSet):
    # custom attributes
    created_from = DateFilter(field_name='date_created', lookup_expr='gte')
    created_to = DateFilter(field_name='date_created', lookup_expr='lte')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Recipe
        fields = ['title']
