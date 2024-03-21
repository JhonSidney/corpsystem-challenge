from rest_framework.views import APIView
from rest_framework.response import Response
from seller.models import Seller
from seller.api.serializers import SellerSerializer

class SellerListAPIView(APIView):
    def get(self, request):
        all_sale = Seller.objects.all()
        serializer = SellerSerializer(all_sale, many=True)
        return Response(serializer.data)