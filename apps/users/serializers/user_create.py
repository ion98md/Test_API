from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.common.validators import PasswordValidator
from ..services import user_service


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, validators=[UniqueValidator(queryset=user_service.get_users())])
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, validators=[PasswordValidator()])
