import django_filters
from django_filters import CharFilter, DateFilter
from .models import Ingredient
from categories.models import Category


class IngredientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Ingredient
        fields = ('category', 'name')
        # category = queryset=Category.objects.filter(type='fd')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

