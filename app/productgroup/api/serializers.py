from rest_framework import serializers
from productgroup.models import ProductGroup
from product.models import Product
from product.api.serializers import ProductSerializer

class ProductGroupSerializer(serializers.ModelSerializer):
    group_id = serializers.ReadOnlyField()  # Apenas leitura
    group_name = serializers.CharField(required=True)  # Campo obrigatório
    category = serializers.CharField(required=True)  # Campo obrigatório
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, required=False)  # Campo opcional

    
    class Meta:
        model = ProductGroup
        fields = ['group_id','group_name','category','products']
        
    def get_group_id(self,obj):
        return str(obj.group_id)
    
    def get_group_name(self,obj):
        return str(obj.group_name)
    
    def get_category(self,obj):
        return str(obj.category)

    def get_products(self,obj):
        products_queryset =  obj.products.all()
        product_serializer =  ProductSerializer(products_queryset, many=True)
        return product_serializer.data