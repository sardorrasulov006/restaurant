
from django.urls import path

from . import views
from apps.restaurant.views import ReservationListView, ReservationCreateView, RestaurantListView, BromDownload

urlpatterns = [
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),  # Bronlarni ko'rish
    path('reservations/create/', ReservationCreateView.as_view(), name='reservation-create'),  # Bron yaratish
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path("reservations_pdf/<int:reservation_id>", BromDownload.as_view(), name='brom-download'),

]