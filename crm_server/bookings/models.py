from django.db import models
from django.contrib.auth.models import User
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

