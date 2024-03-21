from rest_framework.views import APIView
from rest_framework.response import Response
from productgroup.models import ProductGroup
from productgroup.api.serializers import ProductGroupSerializer

class ProductGroupListAPIView(APIView):
    def get(self, request):
        all_productgroup = ProductGroup.objects.all()
        serializer = ProductGroupSerializer(all_productgroup, many=True)
        return Response(serializer.data)