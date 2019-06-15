from django.db import models
from bookings.models import Booking
# Create your models here.


class CarBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, null=True, blank=True)
    pickup_time = models.DateTimeField(null=True, blank=True)
    drop_off_time = models.DateTimeField(null=True, blank=True)
    num_days = models.FloatField(null=True, blank=True)
    car_category = models.CharField(max_length=100, null=True, blank=True)
    insurance_type = models.CharField(max_length=100, null=True, blank=True)
    num_cars = models.CharField(max_length=100, null=True, blank=True)
    net_per_night = models.FloatField(null=True, blank=True)
    total_net = models.FloatField(null=True, blank=True)
    gross_per_night = models.FloatField(null=True, blank=True)
    total_gross = models.FloatField(null=True, blank=True)


