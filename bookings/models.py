from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Location(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

#Lets try to create the Theatre class:
class Theatre(models.Model):
    """based on the location we can add"""
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Show(models.Model):
    theatre = models.ForeignKey(
        Theatre,
        on_delete=models.CASCADE
    )

    movie_name = models.CharField(max_length=100)

    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie_name} - {self.show_time}"
class Seat(models.Model):
    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE
    )

    seat_number = models.CharField(
        max_length=10
    )

    is_booked = models.BooleanField(
        default=False
    )

    booking = models.ForeignKey(
        'Booking',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.seat_number


class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    
    booking_time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username}"
        )
