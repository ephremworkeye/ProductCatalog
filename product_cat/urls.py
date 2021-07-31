from django.urls import path
from .views import CategoryFormSuccessView, CategoryRecordFormView,\
    ProductRecordFormView, ProductFormSuccessView, CategoryCreateView,\
        ProductCreateView, CategoryUpdateView, ProductUpdateView

urlpatterns = [
    path('new_category', CategoryRecordFormView.as_view(), name='category_add'),
    path('product_cat/cat_success', CategoryFormSuccessView.as_view(), name='category_success'),
    path('new_product', ProductRecordFormView.as_view(), name='product_add'),
    path('product_cat/product_success', ProductFormSuccessView.as_view(), name='product_success'),
    path('create_category', CategoryCreateView.as_view(), name='create_category'),
    path('create_product', ProductCreateView.as_view(), name='create_product'),
    path('update_category/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product')
]
