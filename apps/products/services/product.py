from typing import List, Optional, Union

from django.utils.functional import SimpleLazyObject
from decimal import Decimal
from apps.common.types import QuerySetType, ID, empty
from apps.common.utils import is_uuid4
from ..models import Product
from apps.users.models import User

class ProductService:
    def get_all_products(self, *, prefetch_related: Optional[List[str]] = None) -> QuerySetType[Product]:
        product = Product.objects.all()
        if prefetch_related:
            product = product.prefetch_related(*prefetch_related)
        return product

    def get_product_by_id(self, *, product_id: ID) -> Product:
        product = self.get_all_products().get(id=product_id)
        return product

    def get_product(self, *, product: Union[ID, Product]) -> Product:
        if isinstance(product, Product):
            return product

        if is_uuid4(product):
            product = self.get_product_by_id(product_id=product)
            return product

        product = self.get_all_products.get()
        return product

    def create_product(
            self,
            *,
            name: str,
            description: str,
            price: Decimal,
    ) -> Product:
        product = Product(
            name=name,
            description=description,
            price=price,
            )
        product.save()
        return product

    def delete_product(self, *, product: Union[ID, Product]) -> bool:
        product = self.get_product(product=product)
        product.delete()
        return True