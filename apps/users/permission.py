from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission

class LoginPassword(BasePermission):
    """
    Foydalanuvchi faqat telefon raqami +998971032888 va to'g'ri parol bilan login qilishi mumkin.
    """

    def has_permission(self, request, view):
        # Foydalanuvchi yuborgan telefon raqami va parolni tekshirish
        phone = request.data.get('phone')
        password = request.data.get('password')

        # Telefon raqami +998971032888 va parol 'your_password' bo'lsa ruxsat beriladi
        return phone == '+998971032888' and password == 'your_password'


class IsNotAuthenticatedCustom(BasePermission):
    """
    Maxsus ruxsat: foydalanuvchi autentifikatsiya qilinmagan bo'lishi kerak.
    """

    def has_permission(self, request, view):
        # Agar foydalanuvchi autentifikatsiya qilinmagan bo'lsa, ruxsat beriladi
        return not request.user.is_authenticated

