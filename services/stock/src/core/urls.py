from django.urls import path

from .views import ReservationListView, StockListView


urlpatterns = [
    path(
        "api/v1/reservations/", ReservationListView.as_view(), name="reservation-list"
    ),
    path("api/v1/stocks/", StockListView.as_view(), name="stock-list"),
]