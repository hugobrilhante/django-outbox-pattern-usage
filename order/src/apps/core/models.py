from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


@publish([Config(destination='/exchange/saga/order', version="v1", serializer='order_serializer')])
class Order(models.Model):
    STATUS_CHOICES = (
        ("reserve", "Reserve Stock"),
        ("waiting", "Waiting Payment"),
        ("confirmed", "Payment Confirmed"),
        ("rejected", "Out of Stock"),
    )

    order_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=20)
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")
    created = models.DateTimeField(auto_now_add=True)

    def order_serializer(self):
        return {
            "order_id": self.order_id,
            "product_id": self.product_id,
            "reserved_quantity": self.reserved_quantity,
            "status": self.status
        }

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

