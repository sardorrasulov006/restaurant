from apps.users.models import User  # User modelingizni to'g'ri import qiling
from apps.users.serializers import RegisterSerializer, LoginSerializer  # Serializerni import qiling
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={status.HTTP_200_OK: RegisterSerializer,
                   status.HTTP_400_BAD_REQUEST: RegisterSerializer},
    )
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({"error": "Ushbu telefon raqami allaqachon ro'yxatdan o'tgan!"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Serializerdan foydalanish
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Token yaratish
        return Response({

            "message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi!"
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={status.HTTP_200_OK: LoginSerializer,
                   status.HTTP_400_BAD_REQUEST: LoginSerializer},
    )

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = authenticate(request, phone_number=phone_number, password=password)

        if user is not None:
            # Token yaratish
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Muvaffaqiyatli kirdingiz!"
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Noto'g'ri telefon raqami yoki parol!"}, status=status.HTTP_400_BAD_REQUEST)
