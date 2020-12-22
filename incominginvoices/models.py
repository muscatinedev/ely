from django.db import models
from django.urls import reverse

from suppliers.models import Supplier, Article


class Invoice(models.Model):
    invoiceDate = models.DateTimeField(null=True)
    registrationDate = models.DateTimeField(auto_now_add=True, null=True)
    invoiceNumber = models.CharField(max_length=30, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    # TODO order
    total = models.FloatField(default=0)
    totVat = models.FloatField(default=0)
    totalWithWat = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse("incominginvoice-detail",
                       kwargs={"pk": self.pk})  # passing arg through kwargs and call the name of the url

# TODO override the save method to store totals


class InvoiceItem(models.Model):
    VariabiltyType = [
        ('f', 'Fixed'),
        ('v', 'Variable'),
    ]
    ControlType = [
        ('c', 'Controllable'),
        ('n', 'Non Controllable'),
    ]

    costVariability = models.CharField(max_length=12, choices=VariabiltyType, default='v')
    costControllability = models.CharField(max_length=12, choices=VariabiltyType, default='c')

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)

