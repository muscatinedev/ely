import django_filters
from django_filters import CharFilter, DateFilter
from .models import Invoice, InvoiceItem


class RecipeFilter(django_filters.FilterSet):
    # custom attributes
    date_from = DateFilter(field_name='invoiceDate', lookup_expr='gte')
    date_to = DateFilter(field_name='invoiceDate', lookup_expr='lte')
    supplier = CharFilter(field_name='supplier', lookup_expr='icontains')

    class Meta:
        model = Invoice
        fields = ['supplier', 'invoiceNumber']
