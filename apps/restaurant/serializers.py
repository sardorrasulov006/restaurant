# serializers.py
from rest_framework import serializers
from .models import Reservation
from rest_framework import serializers
from .models import Restaurant


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'restaurant', 'start_time', 'number_of_people']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'manzili', 'description', 'image']



