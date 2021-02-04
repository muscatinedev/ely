from django.db import models
from categories.models import Category
from costcenters.models import CostCenter


class GoodAndService(models.Model):
    VariabiltyType = [
        ('f', 'Fixed'),
        ('v', 'Variable'),
    ]
    ControlType = [
        ('c', 'Controllable'),
        ('n', 'Non Controllable'),
    ]

    costVariability = models.CharField(max_length=12, choices=VariabiltyType, default='v', null=True)
    costControllability = models.CharField(max_length=12, choices=VariabiltyType, default='c', null=True)

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    costCenter = models.ForeignKey(CostCenter, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
