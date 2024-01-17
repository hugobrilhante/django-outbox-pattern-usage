from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'quantity_available', 'reserved_quantity', 'last_updated_at')
    search_fields = ('product_id',)
