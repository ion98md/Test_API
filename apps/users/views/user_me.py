from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets, status
from apps.common.types import ID
from rest_framework.request import Request
from rest_framework.response import Response

from apps.users.serializers import UserDetailSerializer, UserEditSerializer, UserCreateSerializer, UserListSerializer
from apps.users.services import user_service


class MeViewSet(viewsets.GenericViewSet):

    #permission_classes = (permissions.IsAuthenticated,)

    custom_serializer_classes = {
        "create": UserCreateSerializer,
        "list": UserListSerializer,
        "partial_update": UserEditSerializer,
        "retrieve": UserDetailSerializer,
    }

    def get_serializer_class(self):
        return self.custom_serializer_classes.get(self.action, UserListSerializer)

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(operation_summary="Get User Profile", tags=["user"])
    def list(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Create User", tags=["user"])
    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = user_service.create_user(**data)
        serializer = UserListSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Delete User", tags=["user"])
    def destroy(self, request: Request, *args, user_id: ID, **kwargs) -> Response:
        user_service.delete_user(user=user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(operation_summary="Edit User Profile", tags=["user"])
    def partial_update(self, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = user_service.edit_user(user=user, **data)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
