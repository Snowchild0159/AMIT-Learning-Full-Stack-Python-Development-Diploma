from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderListCreateAPIView.as_view()),
    path("orders/<int:pk>/", views.OrderDetailAPIView.as_view()),
    path("orders/<int:pk>/status/", views.OrderStatusUpdateAPIView.as_view()),
    path("seller/orders/", views.SellerOrdersAPIView.as_view()),
]
