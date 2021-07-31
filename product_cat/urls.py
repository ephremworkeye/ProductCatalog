from django.urls import path
from .views import CategoryFormSuccessView, CategoryRecordFormView,\
    ProductRecordFormView, ProductFormSuccessView, CategoryCreateView,\
        ProductCreateView, CategoryUpdateView, ProductUpdateView,\
            CategoryDeleteSuccess, ProductDeleteSuccess, ProductDeleteView, CategoryDeleteView, \
                CategoryDetailView, ProductDetailView

urlpatterns = [
    path('new_category', CategoryRecordFormView.as_view(), name='category_add'),
    path('product_cat/cat_success', CategoryFormSuccessView.as_view(), name='category_success'),
    path('new_product', ProductRecordFormView.as_view(), name='product_add'),
    path('product_cat/product_success', ProductFormSuccessView.as_view(), name='product_success'),
    path('create_category', CategoryCreateView.as_view(), name='create_category'),
    path('create_product', ProductCreateView.as_view(), name='create_product'),
    path('update_category/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete_category/<int:pk>', CategoryDeleteView.as_view(), name='delete_category'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('product_cat/delete_category', CategoryDeleteSuccess.as_view(), name='delete_category_success'),
    path('product_cat/delete_product', ProductDeleteSuccess.as_view(), name='delete_product_success'),
    path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
   
]
