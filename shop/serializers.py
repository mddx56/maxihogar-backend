from rest_framework import serializers

from .models import (
    Categorie,
    Sub_Categorie,
    Product_Attribute,
    Product,
    Product_Sku,
    Product_Image,
)


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class Sub_CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Categorie
        fields = "__all__"


class Product_AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Attribute
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class Product_SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Sku
        fields = "__all__"


class Product_ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = "__all__"
