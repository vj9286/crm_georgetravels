from django.db import models
from bookings.models import Booking
# Create your models here.


class CarBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.CharField(null=True, blank=True, max_length=100)
    drop_off_date = models.DateField(null=True, blank=True)
    drop_off_time = models.DateField(null=True, blank=True)
    num_days = models.CharField(max_length=100, null=True, blank=True)
    car_category = models.CharField(max_length=100, null=True, blank=True)
    insurance_type = models.CharField(max_length=100, null=True, blank=True)
    num_cars = models.CharField(max_length=100, null=True, blank=True)
    net_per_night = models.FloatField(null=True, blank=True)
    total_net = models.FloatField(null=True, blank=True)
    gross_per_night = models.FloatField(null=True, blank=True)
    total_gross = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pickup_location = models.CharField(max_length=100, null=True, blank=True)
    drop_off_location = models.CharField(max_length=100, null=True, blank=True)
    rental_company = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    total_car_rental_net = models.FloatField(null=True, blank=True)
    total_car_rental_gross = models.FloatField(null=True, blank=True)
    lead_driver = models.FloatField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
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




