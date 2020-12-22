from django.db import models
from django.urls import reverse

from goodsandservices.models import GoodAndService
from categories.models import Category
from allergens.models import Allergen


class Brand (models.Model):
    name = models.CharField(max_length=50, default='Brand Name', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    goodOrService = models.ForeignKey(GoodAndService, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60, default='Product Name')
    allergens = models.ManyToManyField(Allergen, blank=True)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={'pk': self.pk})  # passing arg through kwargs and call the name of the url

    def __str__(self):
        return self.name
