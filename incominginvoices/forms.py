from django import forms

from .models import *


class InvoiceCreationForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoiceNumber',
            'invoiceDate',
            'supplier'
        ]
