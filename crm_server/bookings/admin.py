from django.contrib import admin
from .models import Booking, CarBookingProxy
from flightbooking.models import Flight, Passenger
import nested_admin
from daterange_filter.filter import DateRangeFilter
from car_booking.models import CarBooking
from django.utils.safestring import mark_safe

# Register your models here.


class PassengerInline(nested_admin.NestedStackedInline):
    model = Passenger
    extra = 0
    fk_name = 'flight'
    fieldsets = (('Passenger Details', {'fields': (('title', 'first_name', 'last_name', 'nationality',
                                                    'gender', 'dob', 'age_group'),), }),
                 )


class FlightInline(nested_admin.NestedStackedInline):
    model = Flight
    extra = 1
    fk_name = 'booking'
    inlines = [PassengerInline]


class PassengerAdmin(admin.ModelAdmin):
    list_display = ['booking_ref', 'booking_name', 'added_date']
    # inlines = [FlightInline]
    search_fields = ('flight__booking__booking_id', 'flight__booking__booking_name', 'first_name', 'middle_name',
                     'last_name')
    list_filter = (('flight__added_date', DateRangeFilter),)
    fieldsets = (("Booking Details", {'fields': (('booking_id', 'booking_name'),)}),)
    change_list_template = 'templates/flight_search_change_list.html'

    def has_add_permission(self, request):
        return False

    def booking_name(self, obj):
        return obj.flight.booking.booking_name

    @mark_safe
    def booking_ref(self, obj):
        return '<a href="/flight_booking/{0}/change/">{1}</a>'.format(obj.flight.booking.id, obj.flight.booking.booking_id)

    booking_ref.allow_tags = True

    def booking_id(self, obj):
        return obj.booking.booking_id

    def added_date(self, obj):
        return obj.flight.added_date



class CarBookingInline(admin.StackedInline):
    model = CarBooking
    extra = 0
    fieldsets = (("Car Info", {'fields': (('car_type', 'country','city'), ('pickup_time', 'drop_off_time'),
                                          ('num_days', 'pickup_location', 'drop_off_location',),
                                          ('car_category', 'rental_company', 'insurance_type'),
                                          ('address', 'num_cars', 'contact_number'))}),
                 ("Cost Info", {'fields': (('net_per_night', 'total_net'), ('gross_per_night', 'total_gross'))}),
                 ("Other Details", {'fields': (('total_car_rental_net', 'total_car_rental_gross', 'lead_driver', 'dob'),
                                               )}),
                 ("To be Filled By Admin", {'fields':(('supplier', 'supplier_ref', 'vat_id', 'balance_due_date'),
                                                      ('booking_date', 'booked_by', 'deposit_paid', 'payment_due'))}))


class CarBookingAdmin(admin.ModelAdmin):
    inlines = [CarBookingInline]
    fieldsets = (("Booking Details", {'fields': (('booking_id', 'booking_name', 'added_date'),)}),)
    readonly_fields = ('booking_id', 'booking_name', 'added_date')


admin.site.register(Passenger, PassengerAdmin)
admin.site.register(CarBookingProxy, CarBookingAdmin)


