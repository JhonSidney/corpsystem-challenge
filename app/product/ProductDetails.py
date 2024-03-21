from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product
from product.api.serializers import ProductSerializer
from django.http import Http404


class ProductDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)