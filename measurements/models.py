from django.db import models


class Uom(models.Model):

    UomType = [
        ('nn', 'Numeric'),
        ('vl', 'Volume'),
        ('wt', 'Weight')

    ]

    type = models.CharField(max_length=20, choices=UomType)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)
