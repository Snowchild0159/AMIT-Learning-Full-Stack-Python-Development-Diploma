from rest_framework.generics import ListCreateAPIView  , RetrieveUpdateDestroyAPIView
from .models import Product 
from .serializers import ProductListSerializer , ProductDetailSerializer
from rest_framework.permissions import IsAuthenticated

class ProductAPIView(ListCreateAPIView) : 
    queryset = Product.objects.filter(is_deleted = False) 
    serializer_class = ProductListSerializer
    
class ProductDetailsAPIView(RetrieveUpdateDestroyAPIView) :
    queryset = Product.objects.filter(is_deleted = False) 
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]
    