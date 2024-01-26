from django.contrib import admin
from .models import Reservation, Stock

admin.site.register(Reservation)
admin.site.register(Stock)
