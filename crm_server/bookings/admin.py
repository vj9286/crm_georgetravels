from django.contrib import admin
from .models import Booking
from flightbooking.models import Flight, Passenger
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.

#
class PassengerInline(NestedStackedInline):
    model = Passenger
    extra = 0
    fk_name = 'flight'


class FlightInline(NestedStackedInline):
    model = Flight
    extra = 1
    fk_name = 'booking'
    fieldsets = (('Flight Details', {'fields': ('airline_name', 'airline_number'),}),
                 ('Other Details', {'fields': ('dep_airport', 'dep_date', 'arr_airport', 'arr_date',
                                                'airline_class')}),
                 )
    inlines = [PassengerInline]


class BookingAdmin(NestedModelAdmin):
    list_display = ['id', 'booking_id', 'booking_name']
    inlines = [FlightInline]


admin.site.register(Booking, BookingAdmin)