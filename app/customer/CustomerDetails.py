from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Customer
from customer.api.serializers import CustomerSerializer
from django.http import Http404


class CustomerDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)