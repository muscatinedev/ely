from django.db import models
from personnels.models import Personnel
from menues.models import MenuItem
from restauranttables.models import Table


class Comande(models.Model):
    restaurantTable = models.ForeignKey(Table, null=True, on_delete=models.SET_NULL)
    weiter = models.ForeignKey(Personnel, null=True, on_delete=models.SET_NULL)
    orderCollectedTime = models.DateTimeField(auto_now_add=True, null=True)
    waitingMinutes = models.IntegerField()


class ComandeItem(models.Model):
    Chron = [
        ('n', 'Now'),
        ('f', 'Follows'),
        ('f2', 'second Follows'),
    ]
    # TODO what about creatin a table active menu

    menuItem = models.ForeignKey(MenuItem, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    request = models.TextField()
    # aseguire
    cronology = models.CharField(max_length=30, null=True, choices=Chron)
