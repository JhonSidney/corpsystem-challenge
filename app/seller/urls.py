from django.urls import path
from .SellerCreate import SellerCreateAPIView
from .SellerDetails import SellerDetailsAPIView
from .SellerList import SellerListAPIView

urlpatterns = [
    path('sellers/', SellerListAPIView.as_view(), name='seller-list'),
    path('sellers/create/', SellerCreateAPIView.as_view(), name='seller-create'),
    path('sellers/<int:pk>/', SellerDetailsAPIView.as_view(), name='seller-list'),

]