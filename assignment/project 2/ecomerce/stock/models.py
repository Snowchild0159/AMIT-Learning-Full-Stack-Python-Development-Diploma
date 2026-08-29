from ecomerce.models import BaseModel
from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Product(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    num_reviews = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    count_in_stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    
    def __str__(self) : 
        return self.name