from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('product_id', 'quantity_available', 'reserved_quantity', 'last_updated_at')
        read_only_fields = ('last_updated_at',)
