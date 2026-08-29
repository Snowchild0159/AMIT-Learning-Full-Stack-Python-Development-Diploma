from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MinLengthValidator

# djangorestframework : add layer on top of djando to make it easy to build api's, MTV to MV and serializer to convert complex data types to json and vice versa

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 ,  validators=[MinLengthValidator(3)]) # , validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="products" , null=True )
    def __str__(self):
        return self.name
    
   
