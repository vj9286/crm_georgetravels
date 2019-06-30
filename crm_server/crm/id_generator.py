import random
from django.db.models.signals import post_save
from bookings.models import Booking
from django.dispatch import receiver


class GenerateID:
    def __init__(self, instance):
        self.model = instance._meta.model
        self.name = instance.booking_name
        self.dt = instance.added_date
        self.model_name = instance._meta.model_name

    @property
    def generate_id(self):
        try:
            latest = self.model.objects.latest('id').id
            latest = '0{0}'.format(latest) if latest < 9 else latest
        except:
            latest = '01'
        rand = random.randint(10, 99)
        first_letter = 'GT'
        uid = '{0}-{1}{2}{3}{4}{5}'.format(first_letter, str(self.name[0:3]).upper(),
                                           (self.dt.month if self.dt.month > 9 else ('0' + str(self.dt.month))),
                                           str(self.dt.year)[2:4],
                                           latest, rand)
        return uid

    @staticmethod
    @receiver(post_save, sender=Booking)
    def id_signal(sender, instance, created, **kwargs):
        if created:
            temp = GenerateID(instance).generate_id
            meta = instance._meta
            meta.model.objects.filter(id=instance.id).update(**{'booking_id': temp})