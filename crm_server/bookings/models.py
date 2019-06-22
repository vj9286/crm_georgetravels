from django.db import models

# Create your models here.


class Booking(models.Model):
    booking_id = models.CharField(max_length=10)
    booking_name = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)
    #booking_agent = models.User

    def __str__(self):
        return self.booking_name


class CarBookingProxy(Booking):
    class Meta:
        proxy = True
        verbose_name = 'Car Booking'


class Notes(models.Model):
    booking = models.ForeignKey(Booking, null=False, on_delete=models.CASCADE)
    content = models.TextField()
