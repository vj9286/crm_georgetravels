from django.contrib import admin
from .models import Booking, CarBookingProxy
from flightbooking.models import Flight, Passenger
import nested_admin
from daterange_filter.filter import DateRangeFilter
from car_booking.models import CarBooking

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
    fieldsets = (('Flight Details', {'fields': (('airline_name', 'airline_number', 'dep_airport',
                                                'arr_airport'),('dep_date', 'arr_date', 'airline_class',),)}),
                 ('Pricing Details', {'fields': (('adult_net', 'adult_tax', 'adult_total', 'adult_gross',
                                                  'adult_gross_tax', 'adult_gross_total'),
                                                 ('youth_net', 'youth_tax', 'youth_total', 'youth_gross',
                                                  'youth_gross_tax', 'youth_gross_total'),
                                                 ('child_net', 'child_tax', 'child_total', 'child_gross',
                                                  'child_gross_tax', 'child_gross_total'), (
                                                  'infant_net', 'infant_tax', 'infant_total', 'infant_gross',
                                                 'infant_gross_tax', 'infant_gross_total'),), },),
                 ('Total Prices', {'fields':(('net', 'gross'),),}),
                 ('To be Filled by Admin', {'fields': (('e_ticket', 'issue_date', 'baggage_allowance',
                                                        'supplier'),), })
                 )
    inlines = [PassengerInline]


class BookingAdmin(nested_admin.NestedModelAdmin):
    list_display = ['booking_id', 'booking_name', 'added_date']
    inlines = [FlightInline]
    search_fields = ('booking_id', 'booking_name')
    list_filter = (('added_date', DateRangeFilter),)
    fieldsets = (("Booking Details", {'fields': (('booking_id', 'booking_name'),)}),)
    change_form_template = 'templates/booking_page.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = dict()
        extra_context['object_id'] = object_id
        return super(BookingAdmin, self).change_view(request, object_id, form_url=form_url,
                                                                extra_context=extra_context)


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


admin.site.register(Booking, BookingAdmin)
admin.site.register(CarBookingProxy, CarBookingAdmin)


