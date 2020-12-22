from django.db import models
from suppliers.models import Article


class Moviment(models.Model):
    movimentDate = models.DateTimeField(auto_now_add=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0)
    quantityInUomIngredient = models.FloatField(default=0)
    price = models.FloatField(default=0)
