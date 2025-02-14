from typing import List, Optional, Union

from apps.common.types import ID, empty
from apps.common.types import QuerySetType
from ..models import User


class UserService:
    @staticmethod
    def create_user(
        *,
        username: str,
        password: str,
        first_name: Optional[str] = "",
        last_name: Optional[str] = "",
        email: Optional[str] = "",
    ) -> User:
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        return user

    def delete_user(self, *, user: Union[ID, User]) -> None:
        user = self.get_user(user=user)
        user.delete()
        return

    def edit_user(
        self,
        *,
        first_name: Optional[str] = empty,
        last_name: Optional[str] = empty,
        email: Optional[str] = empty,
        user: Union[ID, User],
    ) -> User:
        user = self.get_user(user=user)

        if first_name is not empty:
            user.first_name = first_name

        if last_name is not empty:
            user.last_name = last_name

        if email is not empty:
            user.email = email

        user.save()
        return user

    @staticmethod
    def get_users(*, prefetch_related: Optional[List[str]] = None) -> QuerySetType[User]:
        users = User.objects.all()

        if prefetch_related:
            users = users.prefetch_related(*prefetch_related)
        return users

    def get_user(self, *, user: Union[ID, User], prefetch_related: Optional[List[str]] = None) -> User:
        if isinstance(user, User):
            return user
        return self.get_user_by_id(user_id=user, prefetch_related=prefetch_related)

    def get_user_by_id(self, *, user_id: ID, prefetch_related: Optional[List[str]] = None) -> User:
        user = self.get_users(prefetch_related=prefetch_related).get(id=user_id)
        return user

    def set_password(self, *, user: ID, password: str) -> User:
        user = self.get_user(user=user)
        user.set_password(password)
        user.save()
        return user
