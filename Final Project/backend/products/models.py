from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import BaseModel, User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(BaseModel):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(90)],
        help_text="Discount percentage, for example 15 means 15% off"
    )
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma separated, e.g. leather,handmade")
    is_approved = models.BooleanField(default=False)

    def final_price(self):
        # price after discount, calculated on the fly so it never goes stale
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"Image for {self.product.title}"


class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)

    class Meta:
        # one review per user per product
        unique_together = ["product", "user"]

    def __str__(self):
        return f"{self.user.email} - {self.product.title} ({self.rating})"
