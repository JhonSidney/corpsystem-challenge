from django.urls import path
from product.ProductList import ProductListAPIView
from product.ProductCreate import ProductCreateAPIView
from product.ProductDetails import ProductDetailsAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailsAPIView.as_view(), name='product-details')
]