from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from apps.common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(
        db_index=True,
        unique=True,
        max_length=100,
        error_messages={"unique": "A user with that username already exists."},
        verbose_name=_("Username"),
    )
    email = models.CharField(
        unique=True,
        blank=True,
        null=True,
        max_length=100,
        error_messages={"unique": "A user with that email already exists."},
        verbose_name=_("Email"),
    )
    first_name = models.CharField(max_length=30, blank=True, verbose_name=_("First name"))
    last_name = models.CharField(max_length=150, blank=True, verbose_name=_("Last name"))

    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
        verbose_name=_("Staff status"),
    )

    is_superuser = models.BooleanField(
        default=False,
        help_text="Designates that this user has all permissions without explicitly assigning them.",
        verbose_name=_("Superuser status"),
    )

    permissions = ArrayField(models.CharField(max_length=255), default=list, blank=True, verbose_name=_("Permissions"))

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = None
        super(User, self).save(*args, **kwargs)
