from django.db import models


class Table(models.Model):
    tableNumber = models.CharField(max_length=20, null=True)
