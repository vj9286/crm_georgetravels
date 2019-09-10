from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Booking(models.Model):
    booking_id = models.CharField(max_length=15)
    booking_name = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)
    booking_agent = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(null=True, blank=True, choices=((1, "Agent"),
                                                                 (2, "Tour"),
                                                                 (3, "Payment"),
                                                                 (4, "Accounts"),
                                                                 (5, "Ticketing"),
                                                                 (6, "Documentation")), default=1)

    def __str__(self):
        return self.booking_name


class CarBookingProxy(Booking):
    class Meta:
        proxy = True
        verbose_name = 'Car Booking'


class Notes(models.Model):
    booking = models.ForeignKey(Booking, null=False, on_delete=models.CASCADE)
    content = models.TextField()


class History(models.Model):
    operation_choices = (
        (1, 'Created'),
        (2, 'Updated'),
        (3, 'Deleted'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    operation = models.IntegerField(choices=operation_choices)
    remarks = models.CharField(max_length=10000, null=True, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    added_timestamp = models.DateTimeField(auto_now_add=True)


class PaymentReceived(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date_fund_received = models.DateField(blank=True, null=True)
    payment_method = models.CharField(max_length=100,null=True, blank=True)
    transaction_id = models.CharField(max_length=100,null=True, blank=True)
    gross_amount = models.FloatField(default=0.0)
    surcharge = models.FloatField(default=0.0)


class PaymentsMade(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=100,null=True, blank=True)
    supplier_reference = models.CharField(max_length=100,null=True, blank=True)
    payment_method = models.CharField(max_length=100,null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    supplier_amount = models.FloatField(default=0.0)
    supplier_paid = models.FloatField(default=0.0)
    supplier_balance = models.FloatField(default=0.0)
    supplier_balance_date = models.DateField(null=True, blank=True)
    cancellation_date = models.DateField(null=True, blank=True)
    vat_id = models.CharField(null=True, blank=True, max_length=100)


