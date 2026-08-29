from django.db import transaction
from rest_framework import serializers
from products.models import Product
from .models import Order, OrderItem


class OrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class OrderItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="product.title", read_only=True)
    product_id = serializers.IntegerField(source="product.id", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["product_id", "title", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "payment_method", "address", "city", "phone", "total", "items", "created_at"]
        read_only_fields = ["status", "total"]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemInputSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ["payment_method", "address", "city", "phone", "items"]

    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError("The cart is empty.")
        return items

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        user = self.context["request"].user

        # transaction: either the whole order succeeds or nothing is saved
        with transaction.atomic():
            order = Order.objects.create(user=user, **validated_data)
            total = 0
            for item in items_data:
                try:
                    product = Product.objects.select_for_update().get(
                        id=item["product_id"], is_approved=True, is_deleted=False
                    )
                except Product.DoesNotExist:
                    raise serializers.ValidationError(f"Product {item['product_id']} is not available.")

                if item["quantity"] > product.stock:
                    raise serializers.ValidationError(
                        f"Only {product.stock} left of '{product.title}'."
                    )

                price = product.final_price()
                OrderItem.objects.create(
                    order=order, product=product, quantity=item["quantity"], price=price
                )
                product.stock -= item["quantity"]
                product.save()
                total += price * item["quantity"]

            order.total = total
            order.save()
        return order
