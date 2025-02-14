from typing import Union

from django.utils.functional import SimpleLazyObject

from .user import UserService

user_service: Union[UserService, SimpleLazyObject] = SimpleLazyObject(lambda: UserService())
