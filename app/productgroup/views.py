from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from productgroup.models import ProductGroup
from productgroup.api.serializers import ProductGroupSerializer
from rest_framework.decorators import api_view


class ProductGroupListAPIView(APIView):
    def get(self, request):
        all_productgroup = ProductGroup.objects.all()
        serializer = ProductGroupSerializer(all_productgroup, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer =  ProductGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)