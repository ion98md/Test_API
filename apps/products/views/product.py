from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.request import Request
from rest_framework.response import Response

from .. import serializers
from ..services import product_service
from ...common.pagination import CustomNumberPagination
from rest_framework import generics
from ...common.types import ID


class ProductPagination(CustomNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class ProductViewSet(viewsets.GenericViewSet, generics.GenericAPIView):
    custom_serializer_classes = {
        "list": serializers.ProductSerializer,
        "retrieve": serializers.ProductSerializer,
    }
    lookup_url_kwarg = "product_id"
    filter_backends = (SearchFilter,)
    search_fields = ["name", "price"]
    pagination_class = ProductPagination

    def get_serializer_class(self):
        return self.custom_serializer_classes.get(self.action, serializers.ProductSerializer)

    @swagger_auto_schema(operation_summary="Product List ", tags=["Products"])
    def list(self, request: Request, *args, **kwargs) -> Response:
        product = product_service.get_all_products()
        queryset = self.filter_queryset(product)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(product, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Get product by id", tags=["Products"])
    def retrieve(self, request: Request, product_id: ID, **kwargs) -> Response:
        product = product_service.get_product_by_id(product_id=product_id)
        serializer = self.get_serializer(product)
        return Response(serializer.data)
