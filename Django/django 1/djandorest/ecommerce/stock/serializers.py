# from django import forms 
from rest_framework import serializers 
from .models import  Product
from django.contrib.auth.models import User
# class ProductForm(forms.ModelForm)

  
class ProductSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(source ="user.username" , read_only = True)
    
    def validate_name(self , value) : 
        name = value
        if name == "ahmed" : 
            raise serializers.ValidationError("name musn't be ahmed")
        return name
    

    # stock = serializers.IntegerField(write_only = True)
    # user = UserSerializer()
    
    def create(self, validated_data):
        
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    class Meta : 
        model = Product
        ordering = ["-name"]
        # fields = ["name" , "price"]
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer): 
    products = ProductSerializer(many = True)
    class Meta : 
        model = User
        fields = ["first_name" , "last_name" , 'username' , "products"]
      
        