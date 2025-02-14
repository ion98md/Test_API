from typing import Any, Dict, Generic, Iterator, Optional, Tuple, TypeVar, TypedDict
from uuid import UUID

DjangoModel = TypeVar("DjangoModel")


class QuerySetType(Generic[DjangoModel]):  # extra=Iterable):
    """
    This type represents django.db.models.QuerySet interface.
    Defined Types:
        DjangoModel - model instance
        QuerysetType[DjangoModel] - Queryset of DjangoModel instances
        Iterator[DjangoModel] - Iterator of DjangoModel instances
    """

    def __iter__(self) -> Iterator[DjangoModel]:
        ...

    def all(self) -> "QuerySetType[DjangoModel]":
        ...

    def order_by(self, *args: Any) -> "QuerySetType[DjangoModel]":
        ...

    def count(self) -> int:
        ...

    def filter(self, **kwargs: Any) -> "QuerySetType[DjangoModel]":
        ...

    def exclude(self, **kwargs: Any) -> "QuerySetType[DjangoModel]":
        ...

    def get(self, **kwargs: Any) -> DjangoModel:
        ...

    def annotate(self, **kwargs: Any) -> "QuerySetType[DjangoModel]":
        ...

    def first(self) -> Optional[DjangoModel]:
        ...

    def update(self, **kwargs: Any) -> DjangoModel:
        ...

    def delete(self, **kwargs: Any) -> Tuple[int, Dict[str, int]]:
        ...

    def last(self) -> Optional[DjangoModel]:
        ...

    def exists(self) -> bool:
        ...

    def values(self, *args: Any) -> "QuerySetType[DjangoModel]":
        ...

    def values_list(self, *args: Any) -> "QuerySetType[DjangoModel]":
        ...

    def __getitem__(self, index: int) -> DjangoModel:
        ...

    def __len__(self) -> int:
        ...

    def prefetch_related(self, *args: Any) -> "QuerySetType[DjangoModel]":
        ...

    def select_related(self, *args: Any) -> "QuerySetType[DjangoModel]":
        ...


ID = TypeVar("ID", str, UUID)


class Empty:
    ...


empty = Empty()
