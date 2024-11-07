from rest_framework import serializers
from apps.users.models import User  # User modelingizni to'g'ri import qiling
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=15)
    password = serializers.CharField(required=True, write_only=True)

    def validate_phone_number(self, value):
        # Telefon raqamini tekshirish (agar kerak bo'lsa)
        return value

    def validate_password(self, value):
        # Parolni hash qilish (agar kerak bo'lsa)
        # Faqat parolni hash qilamiz
        return make_password(value)  # Hash qilingan parolni qaytaramiz

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        # Bu yerda siz autentifikatsiya qilish jarayonini qo'shishingiz mumkin
        # Misol uchun, parolni tekshirish
        user = authenticate(phone_number=phone_number, password=password)

        if user is None:
            raise serializers.ValidationError("Noto'g'ri telefon raqami yoki parol!")

        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'username', 'password']

    def create(self, validated_data):
        # Parolni hash qilish
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
