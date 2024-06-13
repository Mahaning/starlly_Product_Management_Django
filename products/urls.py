from django.urls import path
from .views import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductListByNameAPIView,
    ProductListByNameAndPriceRangeAPIView,
    ProductListByPriceRangeAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductSoftDeleteAPIView,
    UploadCSVView
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('products/soft-delete/<int:pk>/', ProductSoftDeleteAPIView.as_view(), name='product-soft-delete'),
    path('products/upload_csv/', UploadCSVView.as_view(), name='product-upload-csv'),
    path('products/filter/by-name/', ProductListByNameAPIView.as_view(), name='product-filter-by-name'),
    path('products/filter/by-price-range/', ProductListByPriceRangeAPIView.as_view(), name='product-filter-by-price-range'),
    path('products/filter/', ProductListByNameAndPriceRangeAPIView.as_view(), name='filter-product-list'),
]
