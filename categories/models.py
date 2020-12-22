from django.db import models


class Category(models.Model):
    CatType = [
        ('fd', 'Food'),
        ('nf', 'Non Food'),
        ('se', 'Service'),
    ]

    type = models.CharField(max_length=20, choices=CatType)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

