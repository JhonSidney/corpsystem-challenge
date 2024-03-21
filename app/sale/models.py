from django.db import models
from customer.models import Customer
from product.models import Product
from seller.models import Seller
from uuid import uuid4

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_date = models.DateField()
    associated_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    associated_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)
    sale_status = models.CharField(max_length=50,  choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])
    payment_methods = models.CharField(max_length=100,  choices=[ ('In Cash', 'In Cash'),('1x - Credit Card', '1x - Credit Card'),('2x - Credit Card', '2x - Credit Card'),('3x - Credit Card', '3x - Credit Card'),('4x - Credit Card', '4x - Credit Card')])
    products = models.ManyToManyField(Product, related_name='sales')

    def __str__(self):
        return f"Sale {self.sale_id} by {self.associated_customer}"