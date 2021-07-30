from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'slug', 'price', 'image', 'created_at']
    prepopulated_fields = {'slug', ('name',)}
