from django.db import transaction
from django_outbox_pattern.payloads import Payload

from .models import Order


def callback(payload: Payload):
    with transaction.atomic():
        order_id = payload.body["order_id"]
        status = payload.body["status"]
        order = Order.objects.get(order_id=order_id)
        order.status = status
        order.save()
        payload.save()
