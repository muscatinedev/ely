from django.db import models
from recipes.models import Recipe, RecipeLine
from ingredients.models import Ingredient
from measurements.models import Uom


class Preparation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    preparationDate = models.DateTimeField(auto_now_add=True)
    startTime = models.DateTimeField()
    finishTime = models.DateTimeField()
    serving = models.IntegerField()
    cost = models.FloatField(default=0)


class PreparationLine(models.Model):
    preparation = models.ForeignKey(Preparation, on_delete=models.SET_NULL, null=True)
    recipeLine = models.ForeignKey(RecipeLine, on_delete=models.SET_NULL, null=True)
    # could be less if there is something left

    serving = models.IntegerField()


class PreparationLineItem(models.Model):
    preparationLine = models.ForeignKey(PreparationLine, on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    uom = models.ForeignKey(Uom,  on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
