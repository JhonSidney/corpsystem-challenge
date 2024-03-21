from rest_framework.views import APIView
from rest_framework.response import Response
from productgroup.models import ProductGroup
from productgroup.api.serializers import ProductGroupSerializer
from django.http import Http404


class ProductGroupDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return ProductGroup.objects.get(pk=pk)
        except ProductGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        productgroup = self.get_object(pk)
        serializer = ProductGroupSerializer(productgroup)
        return Response(serializer.data)