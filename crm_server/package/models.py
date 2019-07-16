from django.db import models
from bookings.models import Booking
# Create your models here.


class Package(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    flight_net = models.FloatField(default=0.0)
    flight_net_other = models.FloatField(default=0.0)
    flight_gross = models.FloatField(default=0.0)
    hotel_net = models.FloatField(default=0.0)
    hotel_net_other = models.FloatField(default=0.0)
    hotel_gross = models.FloatField(default=0.0)
    car_net = models.FloatField(default=0.0)
    car_net_other = models.FloatField(default=0.0)
    car_gross = models.FloatField(default=0.0)
    cruise_net = models.FloatField(default=0.0)
    cruise_net_other = models.FloatField(default=0.0)
    cruise_gross = models.FloatField(default=0.0)
    tour_net = models.FloatField(default=0.0)
    tour_net_other = models.FloatField(default=0.0)
    tour_gross = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    created_date = models.DateTimeField(auto_now_add=True)

