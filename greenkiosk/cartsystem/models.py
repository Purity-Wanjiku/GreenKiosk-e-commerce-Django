from django.db import models
from datetime import datetime

# Create your models here.
class AddToCart (models.Model):
    name = models.CharField(max_length = 32)
    quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    payment_method = models.CharField(max_length=50)
    delivery_cost = models.DecimalField(max_digits = 6, decimal_places = 2)
    
    created_at = models.DateTimeField(default=datetime(2023, 6, 18, 16, 35))
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "Add to cart"