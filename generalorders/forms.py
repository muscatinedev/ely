from django import forms
from .models import Order, OrderItem


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderNumber']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'good', 'uom', 'good', 'quantity', 'note']
    note = forms.CharField(widget=forms.Textarea(attrs={'class': ''}))
