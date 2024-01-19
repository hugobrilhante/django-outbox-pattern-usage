from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


@publish([
    Config(destination='/exchange/saga/stock', version="v1", serializer='order_serializer'),
    Config(destination='/exchange/saga/payment', version="v1", serializer='order_serializer')
])
class Order(models.Model):
    STATUS_CHOICES = (
        ("created", "Created"),
        ("reserved", "Reserved"),
        ("not_reserved", "Not Reserved"),
        ("payment_confirmed", "Payment Confirmed"),
        ("payment_denied", "Payment Denied")
    )

    order_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=20)
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    amount = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")
    created = models.DateTimeField(auto_now_add=True)

    def order_serializer(self):
        return {
            "amount": self.amount,
            "customer_id": self.customer_id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "status": self.status
        }

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
