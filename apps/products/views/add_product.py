from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions
from .. import serializers
from ..services import product_service
from ...common.pagination import CustomNumberPagination
from rest_framework import generics
from ...common.types import ID


class ProductPagination(CustomNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class AddProductViewSet(viewsets.GenericViewSet, generics.GenericAPIView):
    custom_serializer_classes = {
        "create": serializers.CreateProductSerializer,
    }
    lookup_url_kwarg = "product_id"
    filter_backends = (SearchFilter,)
    search_fields = ["name", "price"]
    pagination_class = ProductPagination

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.custom_serializer_classes.get(self.action, serializers.ProductSerializer)

    @swagger_auto_schema(operation_summary="Add Product ", tags=["Create Product"])
    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        location = product_service.create_product(**data)

        serializer = serializers.CreateProductSerializer(location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_summary="Delete Product", tags=["Delete Product"])
    def destroy(self, request: Request, *args, product_id: ID, **kwargs) -> Response:
        product_service.delete_product(product=product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
