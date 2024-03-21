from rest_framework.views import APIView
from rest_framework.response import Response
from seller.models import Seller
from seller.api.serializers import SellerSerializer
from django.http import Http404

class SellerDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Seller.objects.get(pk=pk)
        except Seller.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seller = self.get_object(pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)