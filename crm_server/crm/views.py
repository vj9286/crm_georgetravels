from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .constants import SITE_HEADER, BOOKING_TITLE
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from bookings.models import Booking, History, PaymentReceived, PaymentsMade, Notes
from flightbooking.models import Flight, Airline, Passenger
import datetime
from hotel_booking.models import Hotel
from car_booking.models import CarBooking
from django.contrib.contenttypes.models import ContentType
from cruisebooking.models import CruiseHire
from tourbooking.models import TourBooking
from package.models import Package
from django.db.models import Sum
from payments.models import Payments
from django.contrib.auth.models import User


def update_package(instance):
    try:
        package = Package.objects.get(booking_id=instance.booking_id)
    except:
        package = Package.objects.create(booking_id=instance.booking_id)

    package.flight_net = Flight.objects.filter(booking_id=instance.booking_id).aggregate(net=Sum('net'))['net'] or 0
    package.flight_gross = Flight.objects.filter(booking_id=instance.booking_id).aggregate(gross=Sum('gross'))['gross'] or 0
    package.car_net = CarBooking.objects.filter(booking_id=instance.booking_id).aggregate(total_net=Sum('total_net'))['total_net'] or 0
    package.car_gross = CarBooking.objects.filter(booking_id=instance.booking_id).aggregate(total_gross=Sum('total_gross'))['total_gross'] or 0
    package.hotel_net = Hotel.objects.filter(booking_id=instance.booking_id).aggregate(total_net=Sum('total_net'))['total_net'] or 0
    package.hotel_gross = Hotel.objects.filter(booking_id=instance.booking_id).aggregate(total_gross=Sum('total_gross'))['total_gross'] or 0
    package.tour_net = TourBooking.objects.filter(booking_id=instance.booking_id).aggregate(total_net=Sum('total_net'))['total_net'] or 0
    package.tour_gross = TourBooking.objects.filter(booking_id=instance.booking_id).aggregate(total_gross=Sum('total_gross'))['total_gross'] or 0
    package.cruise_net = CruiseHire.objects.filter(booking_id=instance.booking_id).aggregate(net_per_stay=Sum('net_per_stay'))['net_per_stay'] or 0
    package.cruise_gross = CruiseHire.objects.filter(booking_id=instance.booking_id).aggregate(gross_per_stay=Sum('gross_per_stay'))['gross_per_stay'] or 0
    package.total = package.flight_net + package.flight_gross + package.flight_net_other + package.car_net + \
                    package.car_gross + package.car_net_other + package.tour_net + package.tour_gross + \
                    package.tour_net_other + package.hotel_net + package.hotel_net_other + package.hotel_gross + \
                    package.cruise_net + package.cruise_net_other + package.cruise_gross
    package.save()


def check_authorization(function):
    def wrap(request, id,  *args, **kwargs):
        group = request.user.groups.values_list('name', flat=True)
        try:
            if request.user.is_superuser:
                return function(request, id, *args, **kwargs)
            elif 'Agent' in group:
                if Booking.objects.get(id=id).status == 1:
                    return function(request, id, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page, please contact your admin")
            elif 'Tour' in group:
                if Booking.objects.get(id=id).status == 2:
                    return function(request, id, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page, please contact your admin")
            elif 'Payment' in group:
                if Booking.objects.get(id=id).status == 3:
                    return function(request, id, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page, please contact your admin")
            elif 'Accounts' in group:
                if Booking.objects.get(id=id).status == 4:
                    return function(request, id, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page, please contact your admin")
            elif 'Ticketing' in group:
                if Booking.objects.get(id=id).status == 5:
                    return function(request, id, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page, please contact your admin")
            elif 'Documentation' in group:
                if Booking.objects.get(id=id).status == 6:
                    return function(request, id, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page, please contact your admin")
        except Exception as e:
            return HttpResponse("The booking you are trying to get doesn't exist.")
    return wrap


@login_required(login_url='/admin/login')
def homepage(request):
    if not request.user.is_authenticated:
        return redirect('/admin/login/')
    template = 'templates/home_page.html'
    context = {'username':request.user,
               'title': SITE_HEADER, 'booking_title':BOOKING_TITLE}
    return render(request, template, context)


def landing_page(request):
    template = 'templates/landing_page.html'
    context = {'title': SITE_HEADER}
    return render(request, template, context)


def check_float(value):
    try:
        value = float(value)
    except Exception as e:
        return 0
    return value


def date_for_db_formatter(value):
    months = {"January": '01', "February":'02', "March": '03', "April":'04', "May":'05', "June":'06', "July":'07',
              "August": '08', "September":'09', "October": '10', "November":'11', "December":'12'}
    try:
        string = value.split(' ')
    except:
        return None
    try:
        date = string[2] + '-' + months[string[1]] + '-' + string[0]
    except:
        return None
    return date


def check_gender(value):
    if value == 'Male':
        return 'M'
    elif value == 'Female':
        return 'F'
    else:
        return 'N'


def generate_history(*args):
    history = dict()
    history['content_type'] = ContentType.objects.get_for_model(args[0])
    history['object_id'] = args[0].id
    history['operation'] = args[1]
    history['user'] = args[2].user
    history['remarks'] = 'Created'
    if args[1] == 1:
        History.objects.create(**history)
    elif args[1] == 2:
        fields = args[0]._meta.fields
        remarks = ''
        count = 0
        for x in fields:
            old_value = getattr(args[0], x.name)
            new_value = getattr(args[3], x.name)
            if old_value != new_value:
                count +=1
                remarks += str(x.name)+ ':' + 'Old Value:' + str(old_value) + ', New Value: ' + str(new_value)
        history['remarks'] = remarks
        if count > 0:
            History.objects.create(**history)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
def flight_booking_view(request):
    template = 'templates/flight_booking.html'
    context = {}
    flight_booking = dict()
    if request.method == "POST":
        if len(str(request.POST.get('booking_name'))) <= 3:
                return HttpResponse('Booking name is mandatory for booking_id generation and '
                                    'it must be greater than 3 characters ')
        try:
            booking = Booking.objects.create(booking_name=request.POST.get('booking_name'), booking_id='',
                                             booking_agent=request.user)
            flight_booking['booking_id'] = booking.id
            flight_booking['booking_type'] = request.POST.get('livebooking')
            flight_booking['booking_company'] = request.POST.get('worldspan')
            flight_booking['adult_net'] = check_float(request.POST.get('ANfare'))
            flight_booking['adult_tax'] = check_float(request.POST.get('ANtax'))
            flight_booking['adult_total'] = check_float(request.POST.get('ANtotal'))
            flight_booking['youth_net'] = check_float(request.POST.get('YNfare'))
            flight_booking['youth_tax'] = check_float(request.POST.get('YNtax'))
            flight_booking['youth_total'] = check_float(request.POST.get('YNtotal'))
            flight_booking['child_net'] = check_float(request.POST.get('CNnet'))
            flight_booking['child_tax'] = check_float(request.POST.get('CNtax'))
            flight_booking['net'] = check_float(request.POST.get('Net'))
            flight_booking['gross'] = check_float(request.POST.get('Gross'))
            flight_booking['pnr'] = request.POST.get('PNR')
            flight_booking['airline_ref'] = request.POST.get('airline_ref')
            flight_booking['child_total'] = check_float(request.POST.get('CNtotal'))
            flight_booking['infant_net'] = check_float(request.POST.get('INfare'))
            flight_booking['infant_tax'] = check_float(request.POST.get('INtax'))
            flight_booking['infant_total'] = check_float(request.POST.get('INtotal'))
            flight_booking['adult_gross'] = check_float(request.POST.get('Afare'))
            flight_booking['adult_gross_tax'] = check_float(request.POST.get('Atax'))
            flight_booking['adult_gross_total'] = check_float(request.POST.get('Atotal'))
            flight_booking['youth_gross'] = check_float(request.POST.get('Yfare'))
            flight_booking['youth_gross_tax'] = check_float(request.POST.get('Ytax'))
            flight_booking['youth_gross_total'] = check_float(request.POST.get('Ytotal'))
            flight_booking['child_gross'] = check_float(request.POST.get('Cnet'))
            flight_booking['child_gross_tax'] = check_float(request.POST.get('Ctax'))
            flight_booking['child_gross_total'] = check_float(request.POST.get('Ctotal'))
            flight_booking['infant_gross'] = check_float(request.POST.get('Ifare'))
            flight_booking['infant_gross_tax'] = check_float(request.POST.get('Itax'))
            flight_booking['infant_gross_total'] = check_float(request.POST.get('Itotal'))
            flight_booking['e_ticket'] = request.POST.get('Eticket')
            flight_booking['issue_date'] = date_for_db_formatter(request.POST.get('issuedate'))
            flight_booking['baggage_allowance'] = request.POST.get('BaggageAllowance')
            flight_booking['supplier'] = request.POST.get('ASupplier')
            flight = Flight.objects.create(**flight_booking)
            update_package(flight)
            generate_history(flight, 1, request)
            for i in range(0, len(request.POST.getlist('airline'))):
                airline = dict()
                airline['flight_id'] = flight.id
                airline['airline_name'] = request.POST.getlist('airline')[i]
                airline['airline_number'] = request.POST.getlist('anumber')[i]
                airline['dep_airport'] = request.POST.getlist('dpairport')[i]
                airline['dep_date'] = date_for_db_formatter(request.POST.getlist('ddate')[i])
                airline['arr_airport'] = request.POST.getlist('arrairport')[i]
                airline['arr_date'] = date_for_db_formatter(request.POST.getlist('adate')[i])
                airline['airline_class'] = request.POST.getlist('aclass')[i]
                airline['arr_time'] = request.POST.get('atime')
                airline['dep_time'] = request.POST.get('dtime')
                Airline.objects.create(**airline)
                generate_history(flight, 1, request)
            for i in range(0, len(request.POST.getlist('fname'))):
                passenger = dict()
                passenger['flight_id'] = flight.id
                passenger['title'] = request.POST.getlist('title')[i]
                passenger['first_name'] = request.POST.getlist('fname')[i]
                passenger['middle_name'] = request.POST.getlist('mname')[i]
                passenger['last_name'] = request.POST.getlist('lname')[i]
                passenger['nationality'] = request.POST.getlist('nationality')[i]
                passenger['dob'] = date_for_db_formatter(request.POST.getlist('dob')[i])
                passenger['gender'] = check_gender(request.POST.getlist('gender')[i])
                passenger['age_group'] = request.POST.getlist('agegroup')[i]
                Passenger.objects.create(**passenger)
                generate_history(flight, 1, request)
        except Exception as e:
            return HttpResponse(str(e))
        return redirect('/flight_booking/{0}/change'.format(booking.id))
    return render(request, template, context=context)


@csrf_exempt
@login_required(login_url='/admin/login')
@check_authorization
@transaction.atomic
def flight_booking_change_view(request, id):
    flights = Flight.objects.filter(booking_id=id)
    booking = Booking.objects.get(id=id)
    flight_with_pass = dict()
    for count, x in enumerate(flights):
        flight_with_pass[count] = dict()
        flight_with_pass[count]['flight'] = x
        flight_with_pass[count]['passengers'] = Passenger.objects.filter(flight_id=x.id)
        flight_with_pass[count]['airline'] = Airline.objects.filter(flight_id=x.id)
        flight_with_pass[count]['booking'] = booking
        flight_with_pass[count]['booking'] = booking
    template = 'templates/flight_booking_change.html'
    context = dict()
    context['name'] = id
    context['flight_with_pass'] = flight_with_pass
    flight_booking = dict()
    if request.method == "POST":
        flight_booking['booking_id'] = booking.id
        flight_booking['booking_type'] = request.POST.get('livebooking')
        flight_booking['booking_company'] = request.POST.get('worldspan')
        flight_booking['adult_net'] = check_float(request.POST.get('ANfare'))
        flight_booking['adult_tax'] = check_float(request.POST.get('ANtax'))
        flight_booking['adult_total'] = check_float(request.POST.get('ANtotal'))
        flight_booking['youth_net'] = check_float(request.POST.get('YNfare'))
        flight_booking['youth_tax'] = check_float(request.POST.get('YNtax'))
        flight_booking['youth_total'] = check_float(request.POST.get('YNtotal'))
        flight_booking['child_net'] = check_float(request.POST.get('CNnet'))
        flight_booking['child_tax'] = check_float(request.POST.get('CNtax'))
        flight_booking['child_total'] = check_float(request.POST.get('CNtotal'))
        flight_booking['infant_net'] = check_float(request.POST.get('INfare'))
        flight_booking['infant_tax'] = check_float(request.POST.get('INtax'))
        flight_booking['infant_total'] = check_float(request.POST.get('INtotal'))
        flight_booking['adult_gross'] = check_float(request.POST.get('Afare'))
        flight_booking['adult_gross_tax'] = check_float(request.POST.get('Atax'))
        flight_booking['adult_gross_total'] = check_float(request.POST.get('Atotal'))
        flight_booking['youth_gross'] = check_float(request.POST.get('Yfare'))
        flight_booking['youth_gross_tax'] = check_float(request.POST.get('Ytax'))
        flight_booking['youth_gross_total'] = check_float(request.POST.get('Ytotal'))
        flight_booking['child_gross'] = check_float(request.POST.get('Cnet'))
        flight_booking['child_gross_tax'] = check_float(request.POST.get('Ctax'))
        flight_booking['child_gross_total'] = check_float(request.POST.get('Ctotal'))
        flight_booking['infant_gross'] = check_float(request.POST.get('Ifare'))
        flight_booking['infant_gross_tax'] = check_float(request.POST.get('Itax'))
        flight_booking['infant_gross_total'] = check_float(request.POST.get('Itotal'))
        flight_booking['net'] = check_float(request.POST.get('Net'))
        flight_booking['gross'] = check_float(request.POST.get('Gross'))
        flight_booking['pnr'] = request.POST.get('PNR')
        flight_booking['airline_ref'] = request.POST.get('airline_ref')
        flight_booking['e_ticket'] = request.POST.get('Eticket')
        flight_booking['issue_date'] = date_for_db_formatter(request.POST.get('issuedate'))
        flight_booking['baggage_allowance'] = request.POST.get('BaggageAllowance')
        flight_booking['supplier'] = request.POST.get('ASupplier')
        flight_id = request.POST.get('flight_id')
        if flight_id is not None and flight_id !='':
            old_data = Flight.objects.get(id=flight_id)
            Flight.objects.filter(id=flight_id).update(**flight_booking)
            new_data = Flight.objects.get(id=flight_id)
            update_package(new_data)
            generate_history(old_data, 2, request, new_data)
        else:
            flight = Flight.objects.create(**flight_booking)
            update_package(flight)
            generate_history(flight, 1, request)
        exclude_airline = request.POST.getlist('airline_id')
        for i in range(0, len(request.POST.getlist('airline'))):
            airline = dict()
            airline['flight_id'] = flight_id if flight_id is not None else flight.id
            airline['airline_name'] = request.POST.getlist('airline')[i]
            airline['airline_number'] = request.POST.getlist('anumber')[i]
            airline['dep_airport'] = request.POST.getlist('dpairport')[i]
            airline['dep_date'] = date_for_db_formatter(request.POST.getlist('ddate')[i])
            airline['arr_airport'] = request.POST.getlist('arrairport')[i]
            airline['arr_date'] = date_for_db_formatter(request.POST.getlist('adate')[i])
            airline['airline_class'] = request.POST.getlist('aclass')[i]
            try:
                airline_id = request.POST.getlist('airline_id')[i]
                old_data = Airline.objects.get(id=airline_id)
                Airline.objects.filter(id=airline_id).update(**airline)
                new_data = Airline.objects.get(id=airline_id)
                generate_history(old_data, 2, request, new_data)
            except Exception as e:
                a_created = Airline.objects.create(**airline)
                generate_history(a_created, 1, request)
                exclude_airline.append(a_created.id)
        Airline.objects.filter(flight_id=flight_id).exclude(id__in=exclude_airline).delete()
        exclude_list = request.POST.getlist('passenger_id')
        for i in range(0, len(request.POST.getlist('fname'))):
            passenger = dict()
            passenger['flight_id'] = flight_id if flight_id is not None else flight.id
            passenger['title'] = request.POST.getlist('title')[i]
            passenger['first_name'] = request.POST.getlist('fname')[i]
            passenger['middle_name'] = request.POST.getlist('mname')[i]
            passenger['last_name'] = request.POST.getlist('lname')[i]
            passenger['nationality'] = request.POST.getlist('nationality')[i]
            passenger['dob'] = date_for_db_formatter(request.POST.getlist('dob')[i])
            passenger['gender'] = check_gender(request.POST.getlist('gender')[i])
            passenger['age_group'] = request.POST.getlist('agegroup')[i]
            try:
                passenger_id = request.POST.getlist('passenger_id')[i]
                old_data = Passenger.objects.get(id=passenger_id)
                Passenger.objects.filter(id=passenger_id).update(**passenger)
                new_data = Passenger.objects.get(id=passenger_id)
                generate_history(old_data, 2, request, new_data)
            except:
                created = Passenger.objects.create(**passenger)
                generate_history(created, 1, request)
                exclude_list.append(created.id)
        Passenger.objects.filter(flight_id=flight_id).exclude(id__in=exclude_list).delete()
        return redirect('/flight_booking/{0}/change/'.format(id))
    return render(request, template, context=context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
def flight_delete_view(request, booking_id, flight_id):
    flights = Flight.objects.filter(booking_id=booking_id)
    if flights.count()==1:
        return HttpResponse("You can't delete a booking with just one flight,"
                            " else the entire booking will be invalidated, "
                            "create another flight for this booking to delete the current "
                            "flight you were trying to delete")
    else:
        flights.filter(id=flight_id).delete()
    return redirect('/flight_booking/{0}/change/'.format(booking_id))


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def hotel_booking(request, id):
    template = 'templates/hotel_booking.html'
    context = dict()
    context['name'] = id
    context['hotels'] = Hotel.objects.filter(booking_id=id)
    if context['hotels'].count() == 0:
        context['flag'] = True
    else:
        context['flag'] = False
    context['booking'] = Booking.objects.get(id=id)
    if request.method == "POST":
        hotel_meta = Hotel._meta
        fields = Hotel._meta.fields
        hotel = dict()
        hotel['booking_id'] = id
        for x in fields:
            type = hotel_meta.get_field(x.name).get_internal_type()
            if type == 'DateField':
                hotel[x.name] = date_for_db_formatter(request.POST.get(x.name))
            elif type == 'FloatField':
                hotel[x.name] = check_float(request.POST.get(x.name))
            else:
                hotel[x.name] = request.POST.get(x.name)
        hotel_id = request.POST.get('hotel_id')
        hotel['booking_id'] = id
        del hotel['booking']
        if hotel_id is not None and hotel_id !='':
            hotel['id'] = hotel_id
            old_date = Hotel.objects.get(id=hotel_id)
            Hotel.objects.filter(id=hotel_id).update(**hotel)
            new_data = Hotel.objects.get(id=hotel_id)
            update_package(new_data)
            generate_history(old_date, 2, request, new_data)
        else:
            created = Hotel.objects.create(**hotel)
            update_package(created)
            generate_history(created, 1, request)
        return redirect('/hotel_booking/{0}/change/'.format(id))
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
def hotel_delete_view(request, booking_id, hotel_id):
    template = 'templates/error.html'
    context = dict()
    context['error_msg'] = 'You can\'t delete only hotel in the booking , you can make' \
                           'the values zero, add another hotel in order to delete current one'
    if Hotel.objects.filter(booking_id=booking_id, id=hotel_id).count() == 1:
        get_hotel = Hotel.objects.filter(booking_id=booking_id, id=hotel_id).delete()
        return redirect('/hotel_booking/{0}/change/'.format(booking_id))
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def car_booking(request, id):
    template = 'templates/car_booking.html'
    context = dict()
    context['name'] = id
    context['cars'] = CarBooking.objects.filter(booking_id=id)
    context['booking'] = Booking.objects.get(id=id)
    if context['cars'].count() == 0:
        context['flag'] = True
    else:
        context['flag'] = False
    fields = CarBooking._meta.fields
    car_meta = CarBooking._meta
    car = dict()
    if request.method == "POST":
        for x in fields:
            type = car_meta.get_field(x.name).get_internal_type()
            if type == 'DateField':
                car[x.name] = date_for_db_formatter(request.POST.get(x.name))
            elif type == 'FloatField':
                car[x.name] = check_float(request.POST.get(x.name))
            else:
                car[x.name] = request.POST.get(x.name)
        del car['booking']
        car_id = request.POST.get('car_id')
        car['booking_id'] = id
        if car_id is not None and car_id != '':
            car['id'] = car_id
            old_data = CarBooking.objects.get(id=car_id)
            CarBooking.objects.filter(id=car_id).update(**car)
            new_data = CarBooking.objects.get(id=car_id)
            update_package(new_data)
            generate_history(old_data, 2, request, new_data)
        else:
            created = CarBooking.objects.create(**car)
            update_package(created)
            generate_history(created, 1, request)
        return redirect('/car_hire/{0}/change/'.format(id))

    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
def booking_error(request):
    template = 'templates/error.html'
    context = dict()
    context['error_msg'] = 'You must create a booking in order to add a hotel against it,' \
                           ' add airline or passengers first'
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def tours_booking(request, id):
    template = 'templates/tour_booking.html'
    context = dict()
    context['name'] = id
    context['tours'] = TourBooking.objects.filter(booking_id=id)
    context['booking'] = Booking.objects.get(id=id)
    if context['tours'].count() == 0:
        context['flag'] = True
    else:
        context['flag'] = False
    fields = TourBooking._meta.fields
    tour_meta = TourBooking._meta
    tour = dict()
    if request.method == "POST":
        for x in fields:
            type = tour_meta.get_field(x.name).get_internal_type()
            if type == 'DateField':
                tour[x.name] = date_for_db_formatter(request.POST.get(x.name))
            elif type == 'FloatField':
                tour[x.name] = check_float(request.POST.get(x.name))
            else:
                tour[x.name] = request.POST.get(x.name)
        del tour['booking']
        tour_id = request.POST.get('tour_id')
        tour['booking_id'] = id
        if tour_id is not None and tour_id != '':
            tour['id'] = tour_id
            old_data = TourBooking.objects.get(id=tour_id)
            TourBooking.objects.filter(id=tour_id).update(**tour)
            new_data = TourBooking.objects.get(id=tour_id)
            update_package(new_data)
            generate_history(old_data, 2, request, new_data)
        else:
            created = TourBooking.objects.create(**tour)
            update_package(created)
            generate_history(created, 1, request)
        return redirect('/tours/{0}/change/'.format(id))

    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def cruise_booking(request, id):
    template = 'templates/cruise_booking.html'
    context = dict()
    context['name'] = id
    context['cruises'] = CruiseHire.objects.filter(booking_id=id)
    context['booking'] = Booking.objects.get(id=id)
    if context['cruises'].count() == 0:
        context['flag'] = True
    else:
        context['flag'] = False
    fields = CruiseHire._meta.fields
    cruise_meta = CruiseHire._meta
    cruise = dict()
    if request.method == "POST":
        print(request.POST)
        for x in fields:
            type = cruise_meta.get_field(x.name).get_internal_type()
            if type == 'DateField':
                cruise[x.name] = date_for_db_formatter(request.POST.get(x.name))
            elif type == 'FloatField':
                cruise[x.name] = check_float(request.POST.get(x.name))
            else:
                cruise[x.name] = request.POST.get(x.name)
        del cruise['booking']
        cruise_id = request.POST.get('cruise_id')
        cruise['booking_id'] = id
        if cruise_id is not None and cruise_id != '':
            cruise['id'] = cruise_id
            old_data = CruiseHire.objects.get(id=cruise_id)
            CruiseHire.objects.filter(id=cruise_id).update(**cruise)
            new_data = CruiseHire.objects.get(id=cruise_id)
            update_package(new_data)
            generate_history(old_data, 2, request, new_data)
        else:
            created = CruiseHire.objects.create(**cruise)
            update_package(created)
            generate_history(created, 1, request)
        return redirect('/cruise_hire/{0}/change/'.format(id))

    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def package(request, id):
    template = 'templates/package.html'
    context = dict()
    context['name'] = id
    try:
        context['package'] = Package.objects.get(booking_id=id)
    except:
        template = 'templates/error.html'
        context = dict()
        context['error_msg'] = 'Please create a booking in order to visit this page'
        return render(request,template, context)
    context['booking'] = Booking.objects.get(id=id)
    if request.method == "POST":
        context['package'].flight_net_other = check_float(request.POST.get('flight_net_other'))
        context['package'].car_net_other = check_float(request.POST.get('car_net_other'))
        context['package'].tour_net_other = check_float(request.POST.get('tour_net_other'))
        context['package'].cruise_net_other = check_float(request.POST.get('cruise_net_other'))
        context['package'].hotel_net_other = check_float(request.POST.get('hotel_net_other'))
        context['package'].insurance = check_float(request.POST.get('insurance'))
        context['package'].atol = check_float(request.POST.get('atol'))
        context['package'].commission = check_float(request.POST.get('commission'))
        context['package'].admin_charges = check_float(request.POST.get('admin_charges'))
        old_data = Package.objects.get(id=context['package'].id)
        context['package'].save()
        new_data = Package.objects.get(id=context['package'].id)
        generate_history(old_data, 2, request, new_data)
        update_package(new_data)
        return redirect('/package/{0}/change/'.format(id))
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def payment(request, id):
    template = 'templates/payments.html'
    context = dict()
    context['name'] = id
    context['payments'] = Payments.objects.filter(booking_id=id)
    context['booking'] = Booking.objects.get(id=id)
    if context['payments'].count() == 0:
        context['flag'] = True
    else:
        context['flag'] = False
    fields = Payments._meta.fields
    payment_meta = Payments._meta
    payment = dict()
    if request.method == "POST" and request.POST.get('send') == "1":
        print(request.POST)
        for x in fields:
            type = payment_meta.get_field(x.name).get_internal_type()
            if type == 'DateField':
                payment[x.name] = date_for_db_formatter(request.POST.get(x.name))
            elif type == 'FloatField':
                payment[x.name] = check_float(request.POST.get(x.name))
            else:
                payment[x.name] = request.POST.get(x.name)
        del payment['booking']
        del payment['added_date']
        payment_id = request.POST.get('payment_id')
        payment['booking_id'] = id
        if payment_id is not None and payment_id != '':
            payment['id'] = payment_id
            old_data = Payments.objects.get(id=payment_id)
            Payments.objects.filter(id=payment_id).update(**payment)
            new_data = Payments.objects.get(id=payment_id)
            generate_history(old_data, 2, request, new_data)
        else:
            created = Payments.objects.create(**payment)
            update_package(created)
            generate_history(created, 1, request)
        return redirect('/payments/{0}/change/'.format(id))
    elif request.method == "POST" and request.POST.get('send') == "2":
        if context['booking'].status <=6 :
            context['booking'].status = context['booking'].status + 1
            context['booking'].save()
            return ('/admin/flightbooking/passenger/')
        else:
            return HttpResponse("The booking is already in the last queue")
    elif request.method == "POST" and request.POST.get('send') == "3":
        if context['booking'].status != 1:
            context['booking'].status = context['booking'].status - 1
            context['booking'].save()
            return HttpResponseRedirect('/admin/flightbooking/passenger/')
        else:
            return HttpResponse("The booking is already at the lowest level")
    return render(request, template, context)


def history(request, id):
    template = 'templates/history_tracker.html'
    context = dict()
    flights = Flight.objects.filter(booking_id=id).values_list('id', flat=True)
    passengers = Passenger.objects.filter(flight__booking_id=id).values_list('id', flat=True)
    airlines = Airline.objects.filter(flight__booking_id=id).values_list('id', flat=True)
    carbooking = CarBooking.objects.filter(booking_id=id).values_list('id', flat=True)
    context['flight_histories'] = History.objects.filter(content_type__app_label='flightbooking', content_type__model='Flight',
                                              object_id__in=flights)
    context['passengers'] = History.objects.filter(content_type__app_label='flightbooking',
                                                         content_type__model='passenger',
                                                         object_id__in=passengers)
    context['airlines'] = History.objects.filter(content_type__app_label='flightbooking',
                                                 content_type__model='airline',
                                                 object_id__in=airlines)

    context['booking_id'] = Booking.objects.get(id=id).booking_id
    return render(request, template, context)



@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
@check_authorization
def accounts(request, id):
    template = 'templates/accounts.html'
    context = dict()
    context['name'] = id
    context['payments_received'] = PaymentReceived.objects.filter(booking_id=id)
    context['total_gross'] = PaymentReceived.objects.filter(booking_id=id).aggregate(
                                            gross=Sum('gross_amount'))['gross'] or 0
    context['total_surcharge'] = PaymentReceived.objects.filter(booking_id=id).aggregate(
                                            surcharge_total=Sum('surcharge'))["surcharge_total"] or 0
    context['total_supplier_paid'] = PaymentsMade.objects.filter(booking_id=id).aggregate(
                                    supplied_paid_total=Sum('supplier_paid'))["supplied_paid_total"] or 0
    context["total_supplier_due"] = PaymentsMade.objects.filter(booking_id=id).aggregate(
                                    supplier_balance_total=Sum('supplier_balance'))["supplier_balance_total"] or 0
    context['payments_made'] = PaymentsMade.objects.filter(booking_id=id)
    context['booking'] = Booking.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('payment_received_form') == "payment_received_form":
            fields = PaymentReceived._meta.fields
            payment_rec_meta = PaymentReceived._meta
            for i in range(0, len(request.POST.getlist('date_fund_received'))):
                payment_rec = dict()
                for x in fields:
                    type = payment_rec_meta.get_field(x.name).get_internal_type()
                    if type == 'DateField':
                        payment_rec[x.name] = date_for_db_formatter(request.POST.getlist(x.name)[i])
                    elif type == 'FloatField':
                        payment_rec[x.name] = check_float(request.POST.getlist(x.name)[i])
                    else:
                        if x.name=="booking":
                            payment_rec[x.name] = None
                        else:
                            try:
                                payment_rec[x.name] = request.POST.getlist(x.name)[i]
                            except:
                                payment_rec[x.name] = None
                del payment_rec['booking']
                payment_rec['booking_id'] = id
                if payment_rec['id'] is not None and payment_rec['id'] != '':
                    PaymentReceived.objects.filter(id=payment_rec['id']).update(**payment_rec)
                else:
                    PaymentReceived.objects.create(**payment_rec)

        elif request.POST.get('payment_made_form') == "payment_made_form":
            fields = PaymentsMade._meta.fields
            payment_made_meta = PaymentsMade._meta
            for i in range(0, len(request.POST.getlist('supplier_name'))):
                payment_made = dict()
                for x in fields:
                    type = payment_made_meta.get_field(x.name).get_internal_type()
                    if type == 'DateField':
                        payment_made[x.name] = date_for_db_formatter(request.POST.getlist(x.name)[i])
                    elif type == 'FloatField':
                        print(type, x.name)
                        request.POST.getlist(x.name)
                        payment_made[x.name] = check_float(request.POST.getlist(x.name)[i])
                    else:
                        if x.name == "booking":
                            payment_made[x.name] = None
                        else:
                            try:
                                payment_made[x.name] = request.POST.getlist(x.name)[i]
                            except:
                                payment_made[x.name] = None
                del payment_made['booking']
                payment_made['booking_id'] = id
                if payment_made['id'] is not None and payment_made['id'] != '':
                    PaymentsMade.objects.filter(id=payment_made['id']).update(**payment_made)
                else:
                    PaymentsMade.objects.create(**payment_made)

    return render(request, template, context=context)


@csrf_exempt
@login_required(login_url='/admin/login')
def notes(request, id):
    template = 'templates/notes.html'
    context = dict()
    context['name'] = id
    context['notes'] = Notes.objects.filter(booking_id=id)
    if request.method == "POST":
        if request.POST.get('content') != '':
            Notes.objects.create(booking_id=id, content=request.POST.get('content'))
    return render(request, template, context)

def calculate_profit(package):
    temp = dict()
    temp['total_net'] = package.flight_net  + package.car_net  + package.tour_net + package.hotel_net + \
                                package.cruise_net
    temp['total_net_other'] = package.flight_net_other + package.car_net_other + package.tour_net_other +\
                               package.hotel_net_other + package.cruise_net_other
    temp['total_gross'] = package.flight_gross + package.car_gross + package.tour_gross + \
                          package.hotel_gross + package.cruise_gross
    temp['updated_profit'] = temp['total_gross'] - temp['total_net_other']
    return temp


@csrf_exempt
@login_required(login_url='/admin/login')
def profit_report(request):
    template = 'templates/profit_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    context['users'] = User.objects.all().values_list('id', 'username')
    bookings = Booking.objects.all()
    booking = dict()
    for count, x in enumerate(bookings):
        booking[count] = dict()
        booking[count]['booking'] = x
        booking[count]['flights'] = Flight.objects.filter(booking=x).order_by('id')
        booking[count]['package'] = calculate_profit(Package.objects.get(booking=x))
        booking[count]['dep_date'] = Airline.objects.filter(flight_id=booking[count]['flights'][0].id)[0].dep_date
    context['booking'] = booking
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        if request.POST.get('agent') != "All":
            agent = request.POST.get('agent')
            bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                              added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1),
                                              booking_agent_id=agent)
        else:
            bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                              added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))

        booking = dict()
        for count, x in enumerate(bookings):
            booking[count] = dict()
            booking[count]['booking'] = x
            booking[count]['flights'] = Flight.objects.filter(booking=x).order_by('id')
            booking[count]['package'] = calculate_profit(Package.objects.get(booking=x))
            booking[count]['dep_date'] = Airline.objects.filter(flight_id=booking[count]['flights'][0].id)[0].dep_date
        context['booking'] = booking

    return render(request, template, context)



@csrf_exempt
@login_required(login_url='/admin/login')
def agent_profit_report(request):
    template = 'templates/agents_profit_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    context['agents'] = User.objects.all()
    agent_profit = dict()
    for i in context['agents']:
        all_booking = Booking.objects.filter(booking_agent=i)
        agent_profit[i.username] = 0
        for j in all_booking:
            profit = calculate_profit(Package.objects.get(booking=j))['updated_profit']
            agent_profit[i.username] += profit
    context['agent_profit'] = agent_profit
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))

        for i in context['agents']:
            all_booking = Booking.objects.filter(booking_agent=i, added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                                 added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
            agent_profit[i.username] = 0
            for j in all_booking:
                profit = calculate_profit(Package.objects.get(booking=j))['updated_profit']
                agent_profit[i.username] += profit
        context['agent_profit'] = agent_profit
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
def advance_profit_report(request):
    template = 'templates/advance_profit_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    bookings = Booking.objects.all()
    booking = dict()
    for count, x in enumerate(bookings):
        booking[count] = dict()
        booking[count]['booking'] = x
        booking[count]['flights'] = Flight.objects.filter(booking=x).order_by('id')
        booking[count]['package'] = calculate_profit(Package.objects.get(booking=x))
        booking[count]['airline'] = Airline.objects.filter(flight_id=booking[count]['flights'][0].id)[0]
        print(booking[count]['airline'])
    context['booking'] = booking
    if request.method == "POST":
        try:
            start_date = date_for_db_formatter(request.POST.get('from'))
            end_date = date_for_db_formatter(request.POST.get('to'))
            bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                              added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
            booking = dict()
            for count, x in enumerate(bookings):
                booking[count] = dict()
                booking[count]['booking'] = x
                booking[count]['flights'] = Flight.objects.filter(booking=x).order_by('id')
                booking[count]['package'] = calculate_profit(Package.objects.get(booking=x))
                booking[count]['airline'] = Airline.objects.filter(flight_id=booking[count]['flights'][0].id)[0]
            context['booking'] = booking
        except Exception as e:
            return HttpResponse("Please enter from date as well as end date")

    return render(request, template, context)

@csrf_exempt
@login_required(login_url='/admin/login')
def supplier_report(request):
    template = 'templates/supplier_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                          added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
    else:
        bookings = Booking.objects.all()
    booking = dict()
    count = 0
    for x in bookings:
        hotels = Hotel.objects.filter(booking=x).order_by('id')
        tours = TourBooking.objects.filter(booking=x).order_by('id')
        cruises = CruiseHire.objects.filter(booking=x).order_by('id')
        cars = CarBooking.objects.filter(booking=x).order_by('id')
        flights= Flight.objects.filter(booking_id=x)
        if tours.count() > 0:
            for tour in tours:
                booking[count] = dict()
                booking[count]['details'] = tour
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(tour.deposit_paid) + check_float(tour.payment_due)
                booking[count]['dep_date'] = Airline.objects.filter(flight_id=flights[0].id)[0].dep_date
                count += 1
        if cruises.count() > 0:
            for cruise in cruises:
                booking[count] = dict()
                booking[count]['details'] = cruise
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(cruise.deposit_paid) + check_float(cruise.payment_due)
                booking[count]['dep_date'] = Airline.objects.filter(flight_id=flights[0].id)[0].dep_date
                count += 1
        if hotels.count() > 0:
            for hotel in hotels:
                booking[count] = dict()
                booking[count]['details'] = hotel
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(hotel.deposit_paid) + check_float(hotel.payment_due)
                booking[count]['dep_date'] = Airline.objects.filter(flight_id=flights[0].id)[0].dep_date
                count += 1
        if cars.count() > 0:
            for car in cars:
                booking[count] = dict()
                booking[count]['details'] = car
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(car.deposit_paid) + check_float(car.payment_due)
                booking[count]['dep_date'] = Airline.objects.filter(flight_id=flights[0].id)[0].dep_date
                count += 1
    context['booking'] = booking
    return render(request, template, context)



@csrf_exempt
@login_required(login_url='/admin/login')
def payment_made_report(request):
    template = 'templates/payment_made_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                          added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
    else:
        bookings = Booking.objects.all()
    booking = dict()
    count = 0
    for x in bookings:
        pay_made = PaymentsMade.objects.filter(booking_id=x.id)
        if pay_made.count() > 0:
            for pay in pay_made:
                booking[count] = dict()
                booking[count]['details'] = pay
                booking[count]['dep_date'] = Airline.objects.filter(flight_id=Flight.objects.filter(booking_id=x.id)[0])[0].dep_date
                booking[count]['booking'] = x
                count += 1

    context['booking'] = booking
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
def payment_received_report(request):
    template = 'templates/payment_received_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                          added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
    else:
        bookings = Booking.objects.all()
    booking = dict()
    count = 0
    for x in bookings:
        pay_rec = PaymentReceived.objects.filter(booking_id=x.id)
        if pay_rec.count() > 0:
            for pay in pay_rec:
                booking[count] = dict()
                booking[count]['details'] = pay
                booking[count]['booking'] = x
                count += 1

    context['booking'] = booking
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
def product_report(request):
    template = 'templates/product_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                          added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
    else:
        bookings = Booking.objects.all()
    booking = dict()
    count = 0
    for x in bookings:
        hotels = Hotel.objects.filter(booking=x).order_by('id')
        tours = TourBooking.objects.filter(booking=x).order_by('id')
        cruises = CruiseHire.objects.filter(booking=x).order_by('id')
        cars = CarBooking.objects.filter(booking=x).order_by('id')
        flights= Flight.objects.filter(booking_id=x)
        if tours.count() > 0:
            for tour in tours:
                booking[count] = dict()
                booking[count]['product'] = 'tour'
                booking[count]['details'] = tour
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(tour.deposit_paid) + check_float(tour.payment_due)
                booking[count]['client_name'] = Passenger.objects.filter(flight_id=flights[0].id)[0].first_name
                count += 1
        if cruises.count() > 0:
            for cruise in cruises:
                booking[count] = dict()
                booking[count]['product'] = 'cruise'
                booking[count]['details'] = cruise
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(cruise.deposit_paid) + check_float(cruise.payment_due)
                booking[count]['client_name'] = Passenger.objects.filter(flight_id=flights[0].id)[0].dep_date
                count += 1
        if hotels.count() > 0:
            for hotel in hotels:
                booking[count] = dict()
                booking[count]['product'] = 'hotel'
                booking[count]['details'] = hotel
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(hotel.deposit_paid) + check_float(hotel.payment_due)
                booking[count]['client_name'] = Passenger.objects.filter(flight_id=flights[0].id)[0].first_name
                count += 1
        if cars.count() > 0:
            for car in cars:
                booking[count] = dict()
                booking[count]['product'] = 'car'
                booking[count]['details'] = car
                booking[count]['booking'] = x
                booking[count]['flights'] = flights
                booking[count]['supplier_net'] = check_float(car.deposit_paid) + check_float(car.payment_due)
                booking[count]['client_name'] = Passenger.objects.filter(flight_id=flights[0].id)[0].first_name
                count += 1
    context['booking'] = booking
    return render(request, template, context)




@csrf_exempt
@login_required(login_url='/admin/login')
def accounts_report(request):
    template = 'templates/accounts_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                          added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))
    else:
        bookings = Booking.objects.all()
    booking = dict()
    count = 0
    for x in bookings:
        pay_rec = PaymentReceived.objects.filter(booking_id=x.id)
        if pay_rec.count() > 0:
            for pay in pay_rec:
                package_obj = Package.objects.get(booking_id=x.id)
                booking[count] = dict()
                booking[count]['booking_date'] = x.added_date
                booking[count]['customer_name'] = Passenger.objects.filter(flight_id=Flight.objects.filter(booking_id=x.id)[0])[0].first_name
                booking[count]['payment_received'] = PaymentReceived.objects.filter(booking_id=x.id).aggregate(
                    gross=Sum('gross_amount'))['gross'] or 0
                booking[count]['booking'] = x
                booking[count]['total_net'] = calculate_profit(Package.objects.get(booking=x))['total_net']
                booking[count]['total_gross'] = calculate_profit(Package.objects.get(booking=x))['total_gross']
                booking[count]['no_of_passengers'] = Passenger.objects.filter(
                    flight_id__in=Flight.objects.filter(booking_id=x.id).values_list('id', flat=True)).count()
                booking[count]['vat_id'] = "Test"
                booking[count]['package'] = package_obj
                booking[count]['transaction_charge'] = PaymentReceived.objects.filter(booking_id=x.id).aggregate(
                    transaction_charge=Sum('surcharge'))['transaction_charge'] or 0
                count += 1

    context['booking'] = booking
    return render(request, template, context)



@csrf_exempt
@login_required(login_url='/admin/login')
def taps_report(request):
    template = 'templates/taps_report.html'
    context = dict()
    context['username'] = request.user
    context['title'] = SITE_HEADER
    if request.method == "POST":
        start_date = date_for_db_formatter(request.POST.get('from'))
        end_date = date_for_db_formatter(request.POST.get('to'))
        bookings = Booking.objects.filter(added_date__gte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
                                          added_date__lte=datetime.datetime.strptime(end_date, "%Y-%m-%d")+ datetime.timedelta(days=1))
    else:
        bookings = Booking.objects.all()
    booking = dict()
    count = 0
    for x in bookings:
        pay_rec = PaymentReceived.objects.filter(booking_id=x.id)
        pay_made = PaymentsMade.objects.filter(booking_id=x.id)
        if pay_rec.count() > 0:
                package_obj = Package.objects.get(booking_id=x.id)
                booking[count] = dict()
                booking[count]['date_fund_received']=pay_rec.values_list('date_fund_received', flat=True)
                booking[count]['payment_method']=pay_rec.values_list('payment_method', flat=True)
                booking[count]['booking_date'] = x.added_date
                booking[count]['customer_name'] = Passenger.objects.filter(flight_id=Flight.objects.filter(booking_id=x.id)[0])[0].first_name
                booking[count]['payment_received'] = PaymentReceived.objects.filter(booking_id=x.id).aggregate(
                    gross=Sum('gross_amount'))['gross'] or 0
                booking[count]['payment_made'] = pay_made.aggregate(supplier_paid_total=Sum('supplier_paid'))['supplier_paid_total'] or 0
                booking[count]['supplier_name'] = pay_made.values_list('supplier_name', flat=True)
                booking[count]['supplier_pay_method'] = pay_made.values_list('payment_method', flat=True)
                booking[count]['supplier_amount'] = pay_made.aggregate(supplier_amount_total=Sum('supplier_amount'))['supplier_amount_total']
                booking[count]['package'] = package_obj
                count += 1

    context['booking'] = booking
    return render(request, template, context)



# @csrf_exempt
# @login_required(login_url='/admin/login')
# def payment_made_report(request):
#     template = 'templates/payment_made_received.html'
#     context = dict()
#     context['username'] = request.user
#     context['title'] = SITE_HEADER
