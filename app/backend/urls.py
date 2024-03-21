from django.contrib import admin
from django.urls import path, include
from .settings import URL_PREFIX

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{URL_PREFIX}/",include('customer.urls')),
    path(f"{URL_PREFIX}/", include('product.urls')),
    path(f"{URL_PREFIX}/", include('productgroup.urls')),
    path(f"{URL_PREFIX}/", include('sale.urls')),
    path(f"{URL_PREFIX}/", include('seller.urls')),

    ]