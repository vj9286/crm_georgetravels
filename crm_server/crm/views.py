from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .constants import SITE_HEADER, BOOKING_TITLE
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from bookings.models import Booking, History
from flightbooking.models import Flight, Airline, Passenger
import datetime
from hotel_booking.models import Hotel
from car_booking.models import CarBooking
from django.contrib.contenttypes.models import ContentType
from cruisebooking.models import CruiseHire


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
    string = value.split(' ')
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
            generate_history(old_data, 2, request, new_data)
        else:
            flight = Flight.objects.create(**flight_booking)
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
            passenger['flight_id'] = flight_id
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
            generate_history(old_date, 2, request, new_data)
        else:
            created = Hotel.objects.create(**hotel)
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
        print(request.POST)
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
            generate_history(old_data, 2, request, new_data)
        else:
            created = CarBooking.objects.create(**car)
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
def tours_booking(request, id):
    template = 'templates/tour_booking.html'
    context = dict()
    context['name'] = id
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
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
            generate_history(old_data, 2, request, new_data)
        else:
            created = CruiseHire.objects.create(**cruise)
            generate_history(created, 1, request)
        return redirect('/cruise_hire/{0}/change/'.format(id))

    return render(request, template, context)
