from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('is_deleted', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

    def get_queryset(self, request):
        # Include soft-deleted products in the admin panel
        return Product.objects.all()

    def delete_model(self, request, obj):
        # Soft delete the product
        obj.is_deleted = True
        obj.save()

admin.site.register(Product, ProductAdmin)
