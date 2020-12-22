import django_filters
from django_filters import CharFilter, DateFilter
from .models import Invoice, InvoiceItem


class InvoiceFilter(django_filters.FilterSet):
    # custom attributes
    date_from = DateFilter(field_name='invoiceDate', lookup_expr='gte')
    date_to = DateFilter(field_name='invoiceDate', lookup_expr='lte')
    supplier = CharFilter(field_name='supplier__name', lookup_expr='icontains')

    class Meta:
        model = Invoice
        fields = ['invoiceNumber']
