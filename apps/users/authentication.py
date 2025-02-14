from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_friendly_errors.mixins import ErrorMessagesMixin
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import SlidingToken
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from rest_framework import status


class CustomSlidingSerializer(ErrorMessagesMixin, TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return SlidingToken.for_user(user)

    def validate(self, attrs):
        user = authenticate(**{self.username_field: attrs[self.username_field], "password": attrs["password"]})
        self.user = user

        if not user:
            raise BadCredentials(_("Can't login with given credentials"))

        token = self.get_token(self.user)
        data = dict(token=str(token))

        update_last_login(None, self.user)

        return data


class CustomTokenObtainClass(TokenViewBase):
    serializer_class = CustomSlidingSerializer


class BadCredentials(AuthenticationFailed):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = code = "bad_credentials"

