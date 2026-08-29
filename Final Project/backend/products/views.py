from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    ReviewSerializer,
)
from .permissions import IsSellerOrReadOnly, IsOwnerOrReadOnly


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsSellerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "tags", "brand"]
    ordering_fields = ["price", "created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductDetailSerializer
        return ProductListSerializer

    def get_queryset(self):
        # customers only see approved, not-deleted products
        queryset = Product.objects.filter(is_approved=True, is_deleted=False)
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

    def perform_create(self, serializer):
        # the logged in seller becomes the product owner automatically
        serializer.save(seller=self.request.user)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        # soft delete: keep the row so old orders still work
        instance.is_deleted = True
        instance.save()


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["pk"], is_deleted=False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, product_id=self.kwargs["pk"])


class SellerProductListAPIView(generics.ListAPIView):
    # the seller sees all their products, including not yet approved ones
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user, is_deleted=False)
