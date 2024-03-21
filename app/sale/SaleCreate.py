from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from sale.api.serializers import SaleSerializer
from sale.models import Sale

class SaleCreateAPIView(APIView):   
    def post(self,request):
        serializer =  SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    