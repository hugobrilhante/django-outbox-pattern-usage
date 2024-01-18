from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


@publish([Config(destination='/exchange/saga/stock', version="v1")])
class Stock(models.Model):
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Product {self.product_id} - Available: {self.quantity}"
