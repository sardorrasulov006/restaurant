from django.http import HttpResponse

from .serializers import RestaurantSerializer
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ReservationSerializer
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Restaurant, Reservation

from rest_framework.views import APIView

from .utils import generate_pdf
from ..users.models import User


class ReservationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ReservationSerializer,
        responses={
            status.HTTP_201_CREATED: ReservationSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        }
    )
    def post(self, request):
        restaurant_id = request.data.get('restaurant')
        existing_reservation = Reservation.objects.filter(user=request.user, restaurant_id=restaurant_id).first()

        if existing_reservation:
            return Response({"detail": "Siz bu restorandan avval bron qilgansiz."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BromDownload(APIView):
    queryset = Restaurant.objects.all()
    def get(self, request, reservation_id):
        user = request.user
        try:
            reservation = Reservation.objects.get(id=reservation_id)

            if reservation.user == user:
                pdf_reservation = generate_pdf(user, reservation)

                response = HttpResponse(pdf_reservation, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="reservation_{reservation_id}.pdf"'
                return response
            else:
                return Response({"detail": "Sizning broningiz emas"}, status=status.HTTP_403_FORBIDDEN)

        except Reservation.DoesNotExist:
            return Response({"detail": "Bron topilmadi"}, status=status.HTTP_404_NOT_FOUND)


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Foydalanuvchi faqat o'z bronlarini ko'radi
        return Reservation.objects.filter(user=self.request.user)


# Filtrlar uchun
class RestaurantFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')  # Nomi bo'yicha filtr

    class Meta:
        model = Restaurant
        fields = ['name']  # Faqat nom bo'yicha filtr


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RestaurantFilter
    ordering_fields = ['name']
    ordering = ['name']
