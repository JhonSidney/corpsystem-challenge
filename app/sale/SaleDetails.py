from rest_framework.views import APIView
from rest_framework.response import Response
from sale.models import Sale
from sale.api.serializers import SaleSerializer
from django.http import Http404


class SaleDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sale = self.get_object(pk)
        serializer = SaleSerializer(sale)
        return Response(serializer.data)