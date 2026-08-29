from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListAPIView.as_view()),
    path("products/", views.ProductListCreateAPIView.as_view()),
    path("products/<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("products/<int:pk>/reviews/", views.ReviewListCreateAPIView.as_view()),
    path("seller/products/", views.SellerProductListAPIView.as_view()),
]
