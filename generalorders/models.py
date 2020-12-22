from django.db import models
from django.urls import reverse
from categories.models import Category
from suppliers.models import Supplier
from measurements.models import Uom
from goodsandservices.models import GoodAndService


class Order(models.Model):
    Status = [
        ('pe', 'Pending'),
        ('su', 'Submitted'),
        ('ca', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=Status, default='pe')
    orderNumber = models.CharField(max_length=10, null=True)
    orderDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.orderNumber

    def get_absolute_url(self):
        return reverse("generalorder-detail", kwargs={"pk": self.pk})  # passing arg through kwargs and call the name of the url


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    good = models.ForeignKey(GoodAndService, on_delete=models.SET_NULL, null=True)
    uom = models.ForeignKey(Uom, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    note = models.TextField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.good.name
