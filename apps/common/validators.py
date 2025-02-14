from django.contrib.auth import password_validation

from django.core.exceptions import ValidationError as CoreValidationError
from rest_framework.exceptions import ValidationError


class PasswordValidator:
    requires_context = True

    def __call__(self, value, serializer_field):
        try:
            password_validation.validate_password(value)
        except CoreValidationError as error:
            raise ValidationError("".join(error.messages))
