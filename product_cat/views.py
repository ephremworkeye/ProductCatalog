from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView 
from django.views import View
from .forms import CategoryForm, ProductForm
from .models import Category, Product

# Create your views here.
class CategoryRecordFormView(FormView):
    template_name = 'product_cat/category_form.html'
    form_class = CategoryForm
    success_url = '/product_cat/cat_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CategoryFormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Category record saved successfully')

    

class ProductRecordFormView(FormView):
    template_name = 'product_cat/product_form.html'
    form_class = ProductForm
    success_url = '/product_cat/product_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        

class ProductFormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('product record saved successfully')


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'slug']
    template_name = 'product_cat/category_form.html'
    success_url = '/product_cat/cat_success'


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_cat/product_form.html'
    success_url = '/product_cat/product_success'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'slug']
    template_name = 'product_cat/category_form.html'
    success_url = '/product_cat/cat_success'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product_cat/product_form.html'
    success_url = '/product_cat/product_success'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product_cat/category_delete_form.html'
    success_url = '/product_cat/delete_category'


class CategoryDeleteSuccess(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Category item is deleted successfully')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_cat/product_delete_form.html'
    success_url = '/product_cat/delete_product'

class ProductDeleteSuccess(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Product item is deleted successfully')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product_cat/category_detail.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_cat/product_detail.html'

class CategoryList(ListView):
    model = Category
    template_name = 'product_cat/category_detail.html'