from django.db import models
from bookings.models import Booking

# Create your models here.


class Flight(models.Model):
    booking = models.ForeignKey(Booking, null=False, blank=False, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=100, null=True, blank=True)
    booking_company = models.CharField(max_length=100, null=True, blank=True)
    adult_net = models.FloatField(default=0.0)
    adult_tax = models.FloatField(default=0.0)
    adult_total = models.FloatField(default=0.0)
    youth_net = models.FloatField(default=0.0)
    youth_tax = models.FloatField(default=0.0)
    youth_total = models.FloatField(default=0.0)
    child_net = models.FloatField(default=0.0)
    child_tax = models.FloatField(default=0.0)
    child_total = models.FloatField(default=0.0)
    infant_net = models.FloatField(default=0.0)
    infant_tax = models.FloatField(default=0.0)
    infant_total = models.FloatField(default=0.0)
    adult_gross = models.FloatField(default=0.0)
    adult_gross_tax = models.FloatField(default=0.0)
    adult_gross_total = models.FloatField(default=0.0)
    youth_gross = models.FloatField(default=0.0)
    youth_gross_tax = models.FloatField(default=0.0)
    youth_gross_total = models.FloatField(default=0.0)
    child_gross = models.FloatField(default=0.0)
    child_gross_tax = models.FloatField(default=0.0)
    child_gross_total = models.FloatField(default=0.0)
    infant_gross = models.FloatField(default=0.0)
    infant_gross_tax = models.FloatField(default=0.0)
    infant_gross_total = models.FloatField(default=0.0)
    e_ticket = models.CharField(max_length=100, null=True, blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    baggage_allowance = models.CharField(max_length=100, null=True, blank=True)
    net = models.FloatField(default=0.0)
    gross = models.FloatField(default=0.0)
    pnr = models.CharField(max_length=100, blank=True, null=True)
    airline_ref = models.CharField(max_length=100, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking.booking_name


class Airline(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    airline_name = models.CharField(max_length=100, blank=True, null=True)
    airline_number = models.CharField(max_length=100, blank=True, null=True)
    dep_airport = models.CharField(max_length=100, blank=True, null=True)
    dep_date = models.DateField(null=True, blank=True)
    dep_time = models.TimeField(null=True, blank=True)
    arr_airport = models.CharField(max_length=100, null=True, blank=True)
    arr_date = models.DateField(null=True, blank=True)
    arr_time = models.TimeField(null=True, blank=True)
    airline_class = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ['-id']


class Passenger(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TITLE_CHOICES = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Master', 'Master'),
    )
    AGE_GROUP_CHOICES = (
        ('INFANT', 'INFANT'),
        ('KID', 'KID'),
        ('CHILD', 'CHILD'),
        ('ADULT', 'ADULT'),
    )
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='First Name')
    middle_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last Name')
    nationality = models.CharField(max_length=100, null=True, blank=True, default='United Kingdom',
                                   verbose_name='Nationality')
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=100, choices=AGE_GROUP_CHOICES, null=True, blank=True,
                                 verbose_name='Age Group')

    def __str__(self):
        return self.first_name.__str__()

