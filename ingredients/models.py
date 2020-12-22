from django.db import models
from django.urls import reverse

from categories.models import Category
from goodsandservices.models import GoodAndService
from measurements.models import Uom


class Ingredient(GoodAndService):

    uomRef = models.ForeignKey(Uom, on_delete=models.SET_NULL, null=True)
    minimumStock = models.FloatField(default=0, null=True, blank=True)
    quantityInStock = models.FloatField(default=0, blank=True, null=True)
    cal = models.FloatField(default=0)
    car = models.FloatField(default=0)
    pro = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    sta = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient-detail", kwargs={"pk": self.pk})  # passing arg through kwargs and call the name of the url
