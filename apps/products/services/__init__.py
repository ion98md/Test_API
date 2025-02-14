from typing import Union
from django.utils.functional import SimpleLazyObject

from .product import ProductService


product_service: Union[SimpleLazyObject, ProductService] = SimpleLazyObject(lambda: ProductService())

