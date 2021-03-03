from rest_framework import serializers

from api.ingredients.serializers import IngredientSerializer
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']



