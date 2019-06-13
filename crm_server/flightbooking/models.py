from django.db import models
from bookings.models import Booking

# Create your models here.


class Flight(models.Model):
    booking = models.ForeignKey(Booking, null=False, blank=False, on_delete=models.CASCADE)
    airline_name = models.CharField(max_length=100, blank=True, null=True)
    airline_number = models.CharField(max_length=100, blank=True, null=True)
    dep_airport = models.CharField(max_length=100, blank=True, null=True)
    dep_date = models.DateField(null=True, blank=True)
    arr_airport = models.CharField(max_length=100, null=True, blank=True)
    arr_date = models.DateTimeField(null=True, blank=True)
    airline_class = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.airline_name


class Passenger(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name

