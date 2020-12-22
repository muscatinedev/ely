from django.db import models


class Reservation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(null=True)
    name = models.CharField(max_length=40, default='Costumer', null=True)
    pax = models.IntegerField()
    telephone = models.CharField(null=True, max_length=40)
    specialRequest = models.TextField()
