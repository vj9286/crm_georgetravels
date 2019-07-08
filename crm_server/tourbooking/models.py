from django.db import models
from bookings.models import Booking

# Create your models here.


class TourBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    tour_type = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    attraction_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(max_length=100, null=True, blank=True)
    duration = models.FloatField(max_length=100, null=True, blank=True)
    no_of_tickets = models.FloatField(max_length=100, null=True, blank=True)
    net_per_ticket = models.FloatField(default=0.0)
    total_net = models.FloatField(default=0.0)
    gross_per_ticket = models.FloatField(default=0.0)
    total_gross = models.FloatField(default=0.0)
    notes = models.CharField(null=True, blank=True, max_length=100)
    lead_guest = models.CharField(null=True, blank=True, max_length=100)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    supplier_ref = models.CharField(max_length=100, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    booked_by = models.CharField(max_length=100, null=True, blank=True)
    cancellation_date = models.DateField(null=True, blank=True)
    deposit_paid = models.FloatField(default=0.0)
    payment_due = models.FloatField(default=0.0)
    payment_method = models.CharField(null=True, blank=True, max_length=100)
    balance_due_date = models.DateField(null=True, blank=True)
    vat_id = models.CharField(max_length=100, null=True, blank=True)
