from django.db import models
from uuid import uuid4


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    ean_cod = models.IntegerField()

    def __str__(self):
        return self.product_name