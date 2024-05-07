from rest_framework import viewsets

from .models import (
    Categorie,
    Sub_Categorie,
    Product,
    Product_Attribute,
    Product_Image,
    Product_Sku,
)
from .serializers import (
    CategorieSerializer,
    Sub_CategorieSerializer,
    Product_AttributeSerializer,
    ProductSerializer,
    Product_SkuSerializer,
    Product_ImageSerializer,
)


class CategorieView(viewsets.ModelViewSet):
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()


class Sub_CategorieView(viewsets.ModelViewSet):
    serializer_class = Sub_CategorieSerializer
    queryset = Sub_Categorie.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class Product_AttributeView(viewsets.ModelViewSet):
    serializer_class = Product_AttributeSerializer
    queryset = Product_Attribute.objects.all()


class Product_ImageView(viewsets.ModelViewSet):
    serializer_class = Product_ImageSerializer
    queryset = Product_Image.objects.all()


class Product_SkuView(viewsets.ModelViewSet):
    serializer_class = Product_SkuSerializer
    queryset = Product_Sku.objects.all()
