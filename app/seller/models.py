from django.db import models
from uuid import uuid4

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    function = models.CharField(max_length=50,  choices=[('Manager', 'Manager'),('Supervisor','Supervisor'), ('Seller', 'Seller')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"