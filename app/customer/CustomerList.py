from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Customer
from customer.api.serializers import CustomerSerializer

class CustomerListAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)