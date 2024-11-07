

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .validators import validate_phone_number  # Validatorni import qilish
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=25,
        validators=[phone_validator],
        null=True,
        blank=True,
        unique=True
    )
    verification_code = models.CharField(max_length=6, null=True, blank=True)  # Qo'shish kerak
    activation_key_expires = models.DateTimeField(blank=True, null=True)



    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()





