from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import CategoryForm, ProductForm

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

    
    