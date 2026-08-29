from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView
from .models import Student
from .serializers import StudentSerializer 


class StudentAPIView(ListCreateAPIView) : 
    queryset = Student.objects.all()    
    serializer_class = StudentSerializer
    
    