from django.urls import path

from .views import PaymentListView


urlpatterns = [
    path("api/v1/payments/", PaymentListView.as_view(), name="payment-list-create"),
]