from django.db import models

# Create your models here.
class Cost(models.ManyToOneRel):
    VariabiltyType = [
        ('f', 'Fixed'),
        ('v', 'Variable'),
    ]
    ControlType = [
        ('c', 'Controllable'),
        ('n', 'Non Controllable'),
    ]
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.IntegerField()
    costVariability = models.CharField(max_length=12, choices=VariabiltyType, default='v')
    costControllability = models.CharField(max_length=12, choices=VariabiltyType, default='c')
