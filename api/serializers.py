from rest_framework import serializers

from allergens.models import Allergen
from categories.models import Category
from goodsandservices.models import GoodAndService
from personnels.models import *
from products.models import Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    # goodandservices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class GoodAndServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodAndService
        fields = ('name', 'category')


class PersonnelSerializer(serializers.ModelSerializer):
    # goodandservices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Personnel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # goodandservices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    # goodandservices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class AllergenSerializer(serializers.ModelSerializer):
    # goodandservices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Allergen
        fields = '__all__'
