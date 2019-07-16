from django.db import models
from bookings.models import Booking
# Create your models here.


class Payments(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, null=True, blank=True)
    post_code = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    name_on_card = models.CharField(max_length=100, null=True, blank=True)
    expiry_month = models.CharField(max_length=100, null=True, blank=True)
    expiry_year = models.CharField(max_length=100, null=True, blank=True)
    security_code = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    surcharge = models.CharField(max_length=100, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    first_four = models.CharField(max_length=100, null=True, blank=True)
    second_four = models.CharField(max_length=100, null=True, blank=True)
    third_four = models.CharField(max_length=100, null=True, blank=True)
    fourth_four = models.CharField(max_length=100, null=True, blank=True)
    amount_paid = models.FloatField(default=0.0)
    amount_due = models.FloatField(default=0.0)
    due_date = models.DateField(null=True, blank=True)