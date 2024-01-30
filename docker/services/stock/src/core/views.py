from rest_framework import generics
from .models import Reservation, Stock
from .serializers import ReservationSerializer, StockSerializer


class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
