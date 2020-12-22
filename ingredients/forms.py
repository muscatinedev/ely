from django import forms
from .models import Ingredient
from categories.models import Category


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        # fields = '__all__'
        fields = ['category', 'name', 'uomRef', 'cal', 'car', 'pro', 'fat', 'sta',
                  'location', 'costCenter']

    category = forms.ModelChoiceField(required=True, queryset=Category.objects.filter(type='fd'))
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'foodField', 'class': ''}))
    cal = forms.FloatField(label='Calories', required=True)
    car = forms.FloatField(label='CarboHydrates', required=True)
    pro = forms.FloatField(label='Proteins', required=True)
    fat = forms.FloatField(label='Fats', required=True)
    sta = forms.FloatField(label='Starch', required=True)

     # Custom Validation

     # check if exist

    def clean_name(self, *args, **kwargs):
        name_clean = self.cleaned_data.get("name")
        if Ingredient.objects.filter(name=name_clean):
            print('eee')
            raise forms.ValidationError("Already Exist")
        else:
            return name_clean

    def clean_cal(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        cal = self.cleaned_data.get("cal")
        if cal is None:
            return cal
        else:
            if cal < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return cal

    def clean_car(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        car = self.cleaned_data.get("car")
        if car is None:
            return car
        else:
            if car < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return car

    def clean_pro(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        pro = self.cleaned_data.get("pro")
        if pro is None:
            return pro
        else:
            if pro < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return pro

    def clean_fat(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        fat = self.cleaned_data.get("fat")
        if fat is None:
            return fat
        else:
            if fat < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return fat

    def clean_sta(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        sta = self.cleaned_data.get("sta")
        if sta is None:
            return sta
        else:
            if sta < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return sta


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        # fields = '__all__'
        fields = ['category', 'name', 'cal', 'car', 'pro', 'fat', 'sta',
                  'location', 'costCenter', 'location', 'uomRef', 'minimumStock', 'quantityInStock']

    category = forms.ModelChoiceField(required=True, queryset=Category.objects.filter(type='fd'))
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'foodField', 'class': ''}))
    cal = forms.FloatField(label='Calories', required=False)
    car = forms.FloatField(label='CarboHydrates', required=False)
    pro = forms.FloatField(label='Proteins', required=False)
    fat = forms.FloatField(label='Fats', required=False)
    sta = forms.FloatField(label='Starch', required=False)

    # Custom Validation

    def clean_cal(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        cal = self.cleaned_data.get("cal")
        if cal is None:
            return cal
        else:
            if cal < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return cal

    def clean_car(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        car = self.cleaned_data.get("car")
        if car is None:
            return car
        else:
            if car < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return car

    def clean_pro(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        pro = self.cleaned_data.get("pro")
        if pro is None:
            return pro
        else:
            if pro < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return pro

    def clean_fat(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        fat = self.cleaned_data.get("fat")
        if fat is None:
            return fat
        else:
            if fat < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return fat

    def clean_sta(self, *args, **kwargs):
        #  check if is null  null is fine becouse the default value is 0 but  if is null   if cal < 0: does not work
        sta = self.cleaned_data.get("sta")
        if sta is None:
            return sta
        else:
            if sta < 0:
                raise forms.ValidationError("Must be Positive")
            else:
                return sta
