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
