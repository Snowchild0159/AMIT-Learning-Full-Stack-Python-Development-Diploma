from rest_framework.generics import CreateAPIView 
from .serializers import UserSerializer
from .models import User

class UsersAPIView(CreateAPIView) : 
    serializer_class = UserSerializer
    queryset = User.objects.all()