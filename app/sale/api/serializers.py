from rest_framework import serializers
from sale.models import Sale
from product.models import Product
from product.api.serializers import ProductSerializer

class SaleSerializer(serializers.ModelSerializer):
    sale_id = serializers.SerializerMethodField()
    associated_customer = serializers.SerializerMethodField()
    associated_seller = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = ['sale_id','sale_date','associated_customer','associated_seller','sale_value','sale_status','payment_methods','products']

    def get_sale_id(self, obj):
        return str(obj.sale_id)
    
    def get_associated_customer(self, obj):
        return str(obj.associated_customer)
    
    def get_associated_seller(self,obj):
        return str(obj.associated_seller)
    
    def get_products(self, obj):
        products_queryset = obj.products.all()
        product_serializer = ProductSerializer(products_queryset, many=True)
        return product_serializer.data

    def validated(self, validated_data):
        products_data = validated_data.pop('products')  # Remove a lista de produtos dos dados validados
        sale = Sale.objects.create(**validated_data)  # Cria uma instância de Sale com os dados validados

        # Calcula o valor total da venda com base nos produtos associados
        sale_value = 0
        for product_data in products_data:
            product_id = product_data['product_id']
            quantity = product_data.get('quantity', 1)  # Se a quantidade não for especificada, assume 1
            product = Product.objects.get(pk=product_id)
            sale_value += product.price * quantity

        # Atualiza o valor total da venda
        sale.sale_value = sale_value
        sale.save()

        return sale