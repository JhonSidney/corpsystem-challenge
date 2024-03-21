from django.urls import path
from customer.CustomerList import CustomerListAPIView
from customer.CustomerCreate import CustomerCreateAPIView
from customer.CustomerDetails import CustomerDetailsAPIView

urlpatterns = [
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateAPIView.as_view(), name='customer-create'),
    path('customers/<int:pk>/', CustomerDetailsAPIView.as_view(), name='customer-detail')

]