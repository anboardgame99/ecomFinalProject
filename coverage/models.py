from django.db import models
from core.models import Product


# Create your models here.

class Warranty(models.Model):
    warranty_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default="NULL")
    warranty_description = models.TextField()
    warranty_status = models.CharField(max_length=50)
    warranty_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.warranty_id)
