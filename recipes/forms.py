from django import forms

from goodsandservices.models import GoodAndService
from .models import *
from categories.models import Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name',
                  'origin',
                  'title',
                  'shortname',
                  'description',
                  'servings',
                  'preptime',

                  'directions'

                  ]


class RecipeCreationForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'origin',
            'title',
            'title',
            'shortname',
            'description',

            'servings',
            'preptime',
            'cookProgram'

        ]


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'origin',
            'title',
            'title',
            'shortname',
            'description',

            'servings',
            'preptime',
            'cookProgram',
            'directions'
        ]


class RecipeItemsForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ['recipe', 'category', 'ingredient', 'quantity', 'uom', 'destination']

    #

    def __init__(self, *args, **kwargs):
        super(RecipeItemsForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(type='fd').order_by('name')
        #
        self.fields['ingredient'].queryset = Ingredient.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['ingredient'].queryset = Ingredient.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['ingredient'].queryset = self.instance.category.goodOrService_set.order_by('name')


class CookingProgramForm(forms.ModelForm):
    model = CookingProgram
    fields = '__all__'
