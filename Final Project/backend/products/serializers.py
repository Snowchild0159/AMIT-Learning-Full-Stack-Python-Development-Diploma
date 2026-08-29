from django.db.models import Avg
from rest_framework import serializers
from .models import Category, Product, ProductImage, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    final_price = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "title", "price", "discount", "final_price", "brand", "stock", "category", "image"]

    def get_final_price(self, obj):
        return obj.final_price()

    def get_image(self, obj):
        first = obj.images.first()
        if first:
            request = self.context.get("request")
            return request.build_absolute_uri(first.image.url) if request else first.image.url
        return None


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ["id", "user_name", "rating", "comment", "created_at"]

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.email


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    final_price = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    related = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id", "title", "description", "price", "discount", "final_price",
            "stock", "brand", "tags", "category", "category_id",
            "images", "reviews", "average_rating", "related", "is_approved",
        ]
        read_only_fields = ["is_approved"]

    def get_final_price(self, obj):
        return obj.final_price()

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg=Avg("rating"))["avg"]
        return round(avg, 1) if avg else None

    def get_related(self, obj):
        # simple related products: same category, newest first
        related = Product.objects.filter(
            category=obj.category, is_approved=True, is_deleted=False
        ).exclude(id=obj.id)[:4]
        return ProductListSerializer(related, many=True, context=self.context).data
