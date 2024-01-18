from django.db import transaction
from django_outbox_pattern.models import Published
from django_outbox_pattern.payloads import Payload

from .models import Stock


def callback(payload: Payload):
    product_id = payload.body["product_id"]
    quantity = payload.body["quantity"]
    status = payload.body["status"]
    stock = Stock.objects.get(product_id=product_id)
    with transaction.atomic():
        if status == "reserve" and stock.quantity < quantity:
            stock.quantity -= quantity
            stock.save()
        payload.save()
