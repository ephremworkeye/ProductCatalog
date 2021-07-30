from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'