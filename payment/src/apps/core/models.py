import uuid

from django.db import models
from django_outbox_pattern.decorators import Config
from django_outbox_pattern.decorators import publish


@publish([Config(destination='/exchange/saga/payment', version="v1")])
class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.CharField(max_length=20)
    order_id = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="pendent")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.payment_id)
