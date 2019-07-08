from django.db import models
from bookings.models import Booking
# Create your models here.


class Payments(models.Model):
    address = models.CharField(max_length=500, null=True, blank=True)
    post_code = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    name_on_card = models.CharField(max_length=100, null=True, blank=True)
    expiry_date = models.CharField(max_length=100, null=True, blank=True)
    security_code = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    surcharge = models.CharField(max_length=100, null=True, blank=True)
    surcharge = models.CharField(max_length=100, null=True, blank=True)