from django.contrib import admin
from .models import Product
from django.contrib.auth.models import User
# Register your models here.


    
class ProductAdmin(admin.ModelAdmin) : 
    list_display = ['id' , 'name' ,'description' ,  'price' , 'stock' , 'say_hello']
    # list_editable = ["price"]
    fields = ["name" , "stock" , "price" , "description" , 'user']
    def get_queryset(self, request):
        if request.user.is_superuser : 
            return super().get_queryset(request)
        else : 
            return Product.objects.filter(user = request.user)
    def has_change_permission(self, request, obj = None):
        if request.user.is_superuser :
            return True 
        elif obj and  obj.user == request.user : 
            return True 
        else : 
            return False
    def say_hello(self , obj) : 
        return obj.price * obj.stock
    say_hello.short_description = 'Revenue'
    search_fields = ['name__icontains' , 'description']
    list_filter = ["name"]
    list_display_links = ["id" , 'name' ]
    list_per_page = 3
admin.site.register(Product ,ProductAdmin )