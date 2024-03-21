from django.urls import path
from .SaleCreate import SaleCreateAPIView
from .SaleDetails import SaleDetailsAPIView
from .SaleList import SaleListAPIView

urlpatterns = [
    path('sales/', SaleListAPIView.as_view(), name='sales-list'),
    path('sales/create/', SaleCreateAPIView.as_view(), name='sales-create'),
    path('sales/<int:pk>/', SaleDetailsAPIView.as_view(), name='sales-details'),
    path('sales/?<str:seller>/<str:first_name>/<str:last_name>', SaleListAPIView.as_view(), name='sales-filtered-seller'),
    path('sales/?<str:customer>/<str:first_name>/<str:last_name>', SaleListAPIView.as_view(), name='sales-filtered-customer'),
    path('sales/?<str:start>/<str:end>/', SaleListAPIView.as_view(), name='sales-filtered-startDate-endDate'),

]