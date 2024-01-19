from django.db import transaction
from django_outbox_pattern.payloads import Payload

from .models import Payment

PAYMENT_CONFIRMED = 'payment_confirmed'
PAYMENT_DENIED = "payment_denied"
RESERVED = "reserved"


def callback(payload: Payload):
    customer_id = payload.body["customer_id"]
    order_id = payload.body["order_id"]
    amount = payload.body["amount"]
    status = payload.body["status"]
    with transaction.atomic():
        if status == RESERVED:
            payment = Payment(amount=amount, customer_id=customer_id, order_id=order_id)
            if amount < '1000':
                payment.status = PAYMENT_CONFIRMED
            else:
                payment.status = PAYMENT_DENIED
            payment.save()
        payload.save()
