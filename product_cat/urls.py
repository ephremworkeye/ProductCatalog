from django.urls import path
from .views import CategoryFormSuccessView, CategoryRecordFormView

urlpatterns = [
    path('new_category_record', CategoryRecordFormView.as_view(), name='category_record_add'),
    path('product_cat/cat_success', CategoryFormSuccessView.as_view(), name='category_record_success')
]
