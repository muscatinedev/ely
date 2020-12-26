
from rest_framework import serializers
from incominginvoices.models import Invoice, InvoiceItem


class IncominginvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
