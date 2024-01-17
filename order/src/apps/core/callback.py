from django.db import transaction
from django_outbox_pattern.payloads import Payload

def callback(payload: Payload):
    with transaction.atomic():
        payload.save()