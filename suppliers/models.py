from django.db import models
from django.urls import reverse

from products.models import Product


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    vatNumber = models.CharField(max_length=50)
    socialSecurityNumber = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    webSite = models.URLField()
    email = models.EmailField()
    zipCode = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("supplier-detail", kwargs={'pk': self.pk})  # passing arg through kwargs and call the name of the url

    def __str__(self):
        return self.name


class Article(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60, default='Article Name')
