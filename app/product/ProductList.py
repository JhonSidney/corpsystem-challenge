from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product
from product.api.serializers import ProductSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)