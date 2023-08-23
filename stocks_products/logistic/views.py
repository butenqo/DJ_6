from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer, ProductPositionSerializerView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['description', 'title']
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    def get_serializer_class(self):
        subcategory_name = self.request.query_params.get('product')
        if subcategory_name is not None:
            return ProductPositionSerializerView
        else:
            return StockSerializer
    def get_queryset(self):
        queryset = StockProduct.objects.all()
        subcategory_name = self.request.query_params.get('product')
        if subcategory_name is not None:
            queryset = queryset.filter(product=subcategory_name)
            return queryset
        else:
             return Stock.objects.all()


