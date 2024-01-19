from django.db import transaction
from django_outbox_pattern.payloads import Payload

from .models import Order


def callback(payload: Payload):
    order_id = payload.body["order_id"]
    status = payload.body["status"]
    with transaction.atomic():
        order = Order.objects.get(order_id=order_id)
        if not order.status == status:
            order.status = status
            order.save()
        payload.save()
