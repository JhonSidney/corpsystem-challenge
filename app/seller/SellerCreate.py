from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from seller.api.serializers import SellerSerializer

class SellerCreateAPIView(APIView):   
    def post(self,request):
        serializer =  SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)