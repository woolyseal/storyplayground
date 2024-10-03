from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field
from .managers import CustomUserManager
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(
        verbose_name=("Nickname"),
        max_length=128,
        unique=True,
        blank=False,
        null=False,
    )

    email = models.EmailField(
        ("email address"),
        unique=True,
        error_messages={
            "unique": ("The email adress you choose is already in use."),
        },
        blank=False,
    )

    description = CKEditor5Field(verbose_name="Description")

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.nickname

