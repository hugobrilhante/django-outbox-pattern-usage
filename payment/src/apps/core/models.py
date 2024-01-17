import uuid

from django.db import models

class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.UUIDField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="pendent")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.payment_id)
