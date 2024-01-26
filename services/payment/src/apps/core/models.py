import uuid

from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


@publish([Config(destination='/exchange/saga/order', version="v1", serializer='payment_serializer')])
class Payment(models.Model):
    STATUS_CHOICES = (
        ("payment_confirmed", "Payment Confirmed"),
        ("payment_denied", "Payment Denied"),
    )
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.CharField(max_length=20)
    order_id = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def payment_serializer(self):
        return {
            "order_id": self.order_id,
            "status": self.status
        }

    def __str__(self):
        return f"Payment to Order: {self.order_id} - Amount: {self.amount} - Status: {self.status}"
