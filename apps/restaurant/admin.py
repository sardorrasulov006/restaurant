from django.contrib import admin

from apps.restaurant.models import Restaurant, Reservation

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Reservation)



