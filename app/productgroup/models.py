from django.db import models
from product.models import Product
from uuid import uuid4

class ProductGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='groups')

    def __str__(self):
        return self.group_name
