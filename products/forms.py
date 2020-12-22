from django import forms
from .models import Product
from goodsandservices.models import GoodAndService


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['goodOrService'].queryset = GoodAndService.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['goodOrService'].queryset = GoodAndService.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['goodOrService'].queryset = self.instance.category.goodOrService_set.order_by('name')

