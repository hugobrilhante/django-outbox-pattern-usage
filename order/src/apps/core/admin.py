from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "customer_id", "total_amount", "status", "created_at")
    search_fields = ("order_id", "customer_id")
