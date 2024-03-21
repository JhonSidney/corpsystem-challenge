from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','product_name','supplier','price','stock_quantity','ean_cod']
    
    def validate_product_name(self, value):
         if Product.objects.filter(product_name=value).exists():
             raise serializers.ValidationError("try another name!There is a product with this name. ")
         return value

    def validate_ean_cod(self, value):
          if Product.objects.filter(ean_cod=value).exists():
              raise serializers.ValidationError("This product is alredy registered!")
          return value