from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


class Stock(models.Model):
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Product {self.product_id} - Available: {self.quantity}"


@publish([Config(destination='/exchange/saga/order', version="v1", serializer='reservation_serializer')])
class Reservation(models.Model):
    STATUS_CHOICES = (
        ("reserved", "Reserved"),
        ("not_reserved", "Not Reserved"),
        ("payment_denied", "Payment Denied"),
    )
    order_id = models.CharField(max_length=20)
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def reservation_serializer(self):
        return {
            "order_id": self.order_id,
            "status": self.status
        }

    def __str__(self):
        return f"Product {self.product_id} - Order: {self.order_id} - Quantity: {self.quantity} - Status: {self.status}"
