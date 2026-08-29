from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer
        return OrderSerializer

    def get_queryset(self):
        # a user only ever sees their own orders
        return Order.objects.filter(user=self.request.user, is_deleted=False).order_by("-created_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_deleted=False)


class OrderStatusUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        new_status = request.data.get("status")
        valid = [choice[0] for choice in Order.STATUS_CHOICES]
        if new_status not in valid:
            return Response({"detail": f"Status must be one of {valid}."}, status=400)
        try:
            order = Order.objects.get(pk=pk, is_deleted=False)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=404)

        # only staff or a seller who has a product in this order can update it
        is_seller_of_order = order.items.filter(product__seller=request.user).exists()
        if not (request.user.is_staff or is_seller_of_order):
            return Response({"detail": "Not allowed."}, status=403)

        order.status = new_status
        order.save()
        return Response(OrderSerializer(order).data)


class SellerOrdersAPIView(generics.ListAPIView):
    # orders that contain at least one of my products
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            items__product__seller=self.request.user, is_deleted=False
        ).distinct().order_by("-created_at")
