from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
import re


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Telefon raqami va parol orqali foydalanuvchini yaratadi.
        """
        if not phone_number:
            raise ValueError("Telefon raqami kiritilishi kerak.")

        # Telefon raqamini normallashtirish
        phone_number = self.normalize_phone_number(phone_number)

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)  # Parolni o'rnatish
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Superuser yaratadi.
        Superuser uchun is_staff va is_superuser maydonlarini to'g'rilaydi.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser yaratish uchun is_staff=True bo'lishi kerak.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser yaratish uchun is_superuser=True bo'lishi kerak.")

        return self.create_user(phone_number, password, **extra_fields)

    def normalize_phone_number(self, phone_number):
        """
        Telefon raqamini normallashtiradi.
        Bu yerda telefon raqamini kerakli formatga o'tkazish mumkin.
        """
        # Telefon raqamini normallashtirish. Misol: +998901234567 -> 998901234567
        if phone_number.startswith("+"):
            return phone_number  # Telefon raqami allaqachon normallashtirilgan
        return f"+{phone_number}"  # Telefon raqamini normallashtirish
