from django.contrib import admin
from .models import Product
# Register your models here.

# Registering Product Model
class ProductAdmin(admin.ModelAdmin):
    list_display = ['excerpt', ]

    def excerpt(self, obj):
        return obj.get_excerpt(5)
    # pass

admin.site.register(Product, ProductAdmin) 