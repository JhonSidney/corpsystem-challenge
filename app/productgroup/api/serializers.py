from rest_framework import serializers
from productgroup.models import ProductGroup
from product.api.serializers import ProductSerializer

class ProductGroupSerializer(serializers.ModelSerializer):
    group_id = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()
    category =  serializers.SerializerMethodField()
    products =  serializers.SerializerMethodField()
    
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