from django.urls import path
from .ProductGroupCreate import ProductGroupCreateAPIView
from .ProductGroupDetails import ProductGroupDetailsAPIView
from .ProductGroupList import ProductGroupListAPIView

urlpatterns = [
    path('productgroups/', ProductGroupListAPIView.as_view(), name='customer-list'),
    path('productgroups/create/', ProductGroupCreateAPIView.as_view(), name='customer-create'),
    path('productgroups/<int:pk>/', ProductGroupDetailsAPIView.as_view(), name='customer-detail')

]