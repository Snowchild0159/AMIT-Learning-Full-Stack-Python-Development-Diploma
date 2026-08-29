from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Product 
from .serializers import ProductSerializer
# from django.contrib.auth import login , logout , authenticate
# Create your views here.
@api_view(["GET" , "POST"])
def get_products(request) : 
    print(request.user)
    if request.method == "POST" : 
        data = request.data 
        serializer = ProductSerializer(data = data) 
        if serializer.is_valid() :
            serializer.save() 
            return Response(serializer.data , status=200) 
        else : 
            return Response(serializer.errors , status=400)
    products = Product.objects.all() 
    
    serializer = ProductSerializer(products , many=  True )
    
    return Response(serializer.data)
    # data = list(Product.objects.values())
    # repsonse_data = {
    #     "data": data
    # }
    
@api_view(["GET" , "PUT" , 'DELETE']) 
def product_details(request , id) : 
    product = Product.objects.filter(id = id).first() 
    if product : 
        if request.method == "GET" :
                serializer = ProductSerializer(product) 
                return Response(serializer.data) 
        elif request.method == "PUT" : 
            data = request.data
            serializer = ProductSerializer(data = data , instance = product) 
            if serializer.is_valid() : 
                
                serializer.save() 
                return Response(serializer.data , status=200)
            else : 
                return Response({"errors" : serializer.errors} , status=400)
        else : 
            
            product.delete()
            return Response({"detail" : "deleted successfully" } , status=200)
    else : 
        return Response({"details" : "product not found"} , status=404)

# @api_view(["GET"])
# def get_users(request) : 
from rest_framework.views import APIView 
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserAPIView(APIView) : 
    def get(self , request) : 
        users = User.objects.all()
        serializer = UserSerializer(users , many= True) 
        return Response(serializer.data)
    
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView , ListAPIView  , CreateAPIView

class UserGenericAPIView(ListCreateAPIView ) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class UserDetailGenericAPIView(RetrieveUpdateDestroyAPIView ) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    parser_classes = []
    pagination_class = []
    renderer_classes = []
    
    
import jwt    
secret_key = "https://teams.microsoft.com/meet/35035927579884?p=aSIJGtTsttQzmfzHZR"

@api_view(["POST"])
def jwt_login(request) : 
    data = request.data 
    
    username = data.get("username")
    password = data.get("password")
    
    # user = User.objects.filter(username = username , password = password) 
    user = User.objects.filter(username = username ).first()
    if user and user.check_password(password) : 
        data = {
            "first_name" : user.first_name , 
            "last_name" : user.last_name , 
            "id" : user.id , 
            "username": user.username  
        }
    
        token = jwt.encode(data , secret_key , algorithm="HS256")
        
        return Response({
            "token" : token
        })
    else : 
        return Response(status=403)

@api_view(["GET"])
def get_user_data(request) : 
    try : 
        print(request.user)
        # token = request.data.get("token") 
        token = request.headers.get("token")
        
        data = jwt.decode(token , secret_key , algorithms=["HS256"]) 
        
        return Response(data)
    except : 
        return Response(status=401)