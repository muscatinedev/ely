from django.forms import ModelForm
from .models import Allergen


class AllergenForm(ModelForm):
    class Meta:
        model = Allergen
        fields = '__all__'
