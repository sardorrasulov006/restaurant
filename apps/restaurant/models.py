from django.db import models
from apps.users.models import User
from django_resized import ResizedImageField

class Restaurant(models.Model):
    name = models.CharField(    max_length=100)
    manzili = models.CharField(max_length=200)
    description = models.TextField()
    image = ResizedImageField(size=[800, 600], upload_to='images', crop=['middle', 'center'], quality=90)
    def __str__(self):
        return self.name



class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    start_time = models.DateTimeField()  # Bu yerda start_time maydoni
    number_of_people = models.PositiveIntegerField()
    pdf_file = models.FileField(upload_to='reservations/pdfs/', null=True, blank=True)  # PDF maydoni


    def __str__(self):
        return f"{self.user} - {self.restaurant} - {self.start_time}"




