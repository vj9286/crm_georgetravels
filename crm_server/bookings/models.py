from django.db import models

# Create your models here.


class Booking(models.Model):
    booking_id = models.CharField(max_length=10)
    booking_name = models.CharField(max_length=50)
    #booking_agent = models.User


class Notes(models.Model):
    booking = models.ForeignKey(Booking, null=False, on_delete=models.CASCADE)
    content = models.TextField()
