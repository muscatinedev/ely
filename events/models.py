from django.db import models
from personnels.models import Personnel
from menues.models import Menu


class Event(models.Model):
    name = models.CharField(max_length=80)
    date = models.DateTimeField(null=True)
    startAt = models.DateTimeField(null=True)
    expectedEndAt = models.DateTimeField(null=True)
    associatedMenu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
    personnelles = models.ManyToManyField(Personnel)
    cost = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
