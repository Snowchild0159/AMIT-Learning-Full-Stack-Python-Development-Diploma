from django.contrib import admin
from .models import Category, Product, ProductImage, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "seller", "category", "price", "stock", "is_approved", "is_deleted"]
    list_filter = ["is_approved", "category", "is_deleted"]
    search_fields = ["title", "brand", "tags"]
    inlines = [ProductImageInline]
    actions = ["approve_products", "reject_products"]

    @admin.action(description="Approve selected products")
    def approve_products(self, request, queryset):
        queryset.update(is_approved=True)

    @admin.action(description="Reject selected products")
    def reject_products(self, request, queryset):
        queryset.update(is_approved=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Review)
