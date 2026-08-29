from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="users/", null=True, blank=True)
    is_seller = models.BooleanField(default=False)

    # login with email instead of username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=255, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True, default="Egypt")

    def __str__(self):
        return f"{self.user.email} profile"
