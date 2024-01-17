from django.db import models


class Order(models.Model):
    STATUS_CHOICES = (
        ("pendent", "Pendent"),
        ("confirmed", "Confirmed"),
    )

    order_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=255, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendent")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
