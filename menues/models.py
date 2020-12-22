from django.db import models
from recipes.models import Recipe


class Menu(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class MenuSection(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()


class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.SET_NULL, null=True)
    dish = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    costLastCalculated = models.FloatField()
