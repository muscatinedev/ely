from django.db import models
from suppliers.models import Supplier, Article


class Order(models.Model):
    orderNumber = models.CharField(max_length=10, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    note = models.TextField()
