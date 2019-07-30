from django.contrib import admin
from .models import Booking, CarBookingProxy
from flightbooking.models import Flight, Passenger
import nested_admin
from daterange_filter.filter import DateRangeFilter
from car_booking.models import CarBooking
from django.utils.safestring import mark_safe
from django.db.models import Sum
from package.models import Package


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
    list_display = ['booking_ref', 'booking_name', 'added_date', 'history_tracker']
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
        return '<a href="/flight_booking/{0}/change/">{1}</a>'.format(obj.flight.booking.id,
                                                                      obj.flight.booking.booking_id)

    booking_ref.allow_tags = True

    @mark_safe
    def history_tracker(self, obj):
        return '<a href="/history/{0}/change/">Track History</a>'.format(obj.flight.booking.id)

    history_tracker.allow_tags = True

    def booking_id(self, obj):
        return obj.booking.booking_id

    def added_date(self, obj):
        return obj.flight.added_date

    def get_queryset(self, request):
        group = request.user.groups.values_list('name', flat=True)
        qs = super(PassengerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif 'Agent' in group:
            qs = qs.filter(flight__booking__booking_agent=request.user)
            return qs
        else:
            return qs




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

class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'flight_net', 'flight_net_other', 'flight_gross', 'car_net', 'car_net_other',
                    'car_gross', 'cruise_net', 'cruise_net_other', 'cruise_gross', 'tour_net', 'tour_net_other',
                    'tour_gross', 'hotel_net', 'hotel_net_other', 'hotel_gross', 'total']
    change_list_template = 'templates/test_report.html'

    def flight_net(self, obj):
        self.package = Package.objects.get(booking_id=obj.id)
        return self.package.flight_net

    def flight_gross(self, obj):
        return self.package.flight_gross

    def flight_net_other(self, obj):
        return self.package.flight_net_other

    def car_net(self, obj):
        return self.package.car_net

    def car_net_other(self, obj):
        return self.package.car_net_other

    def car_gross(self, obj):
        return self.package.car_gross

    def cruise_net(self, obj):
        return self.package.cruise_net

    def cruise_net_other(self, obj):
        return self.package.cruise_net_other

    def cruise_gross(self, obj):
        return self.package.cruise_gross

    def tour_net(self, obj):
        return self.package.tour_net

    def tour_net_other(self, obj):
        return self.package.tour_net_other

    def tour_gross(self, obj):
        return self.package.tour_gross

    def hotel_net(self, obj):
        return self.package.hotel_net

    def hotel_net_other(self, obj):
        return self.package.hotel_net_other

    def hotel_gross(self, obj):
        return self.package.hotel_gross

    def total(self, obj):
        return self.package.total

    def has_add_permission(self, request):
        return False


admin.site.register(Passenger, PassengerAdmin)
admin.site.register(CarBookingProxy, CarBookingAdmin)
admin.site.register(Booking, BookingAdmin)


