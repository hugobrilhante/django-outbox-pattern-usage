from django.urls import path

from .views import OrderListCreateView


urlpatterns = [
    path("api/v1/orders/", OrderListCreateView.as_view(), name="order-list-create"),
]