from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "first_name", "last_name", "is_seller", "is_active"]
    list_filter = ["is_seller", "is_active"]
    fieldsets = UserAdmin.fieldsets + (
        ("Mahally info", {"fields": ("phone", "photo", "is_seller")}),
    )


admin.site.register(Profile)
