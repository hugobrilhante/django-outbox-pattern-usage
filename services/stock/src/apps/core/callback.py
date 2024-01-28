from django.db import transaction
from django_outbox_pattern.payloads import Payload

from .models import Reservation, Stock

CREATED = "created"
PAYMENT_DENIED = "payment_denied"
RESERVED = "reserved"
NOT_RESERVED = "not_reserved"


def callback(payload: Payload):
    product_id = payload.body["product_id"]
    order_id = payload.body["order_id"]
    quantity = payload.body["quantity"]
    status = payload.body["status"]
    with transaction.atomic():
        stock = Stock.objects.get(product_id=product_id)
        try:
            reservation = Reservation.objects.get(
                product_id=product_id, order_id=order_id
            )
        except Reservation.DoesNotExist:
            reservation = Reservation(
                product_id=product_id, order_id=order_id, quantity=quantity
            )
        if status == CREATED:
            if quantity <= stock.quantity:
                stock.quantity -= quantity
                reservation.status = RESERVED
            else:
                reservation.status = NOT_RESERVED
            reservation.save()
        elif status == PAYMENT_DENIED:
            stock.quantity += quantity
            reservation.status = PAYMENT_DENIED
            reservation.save()
        stock.save()
        payload.save()
