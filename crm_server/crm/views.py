from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .constants import SITE_HEADER, BOOKING_TITLE
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from bookings.models import Booking
from flightbooking.models import Flight, Airline, Passenger
import datetime


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
        return 'Gender'


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
            Flight.objects.filter(id=flight_id).update(**flight_booking)
        else:
            flight_id = Flight.objects.create(**flight_booking).id
        exclude_ariline = request.POST.getlist('airline_id')
        for i in range(0, len(request.POST.getlist('airline'))):
            airline = dict()
            airline['flight_id'] = flight_id
            airline['airline_name'] = request.POST.getlist('airline')[i]
            airline['airline_number'] = request.POST.getlist('anumber')[i]
            airline['dep_airport'] = request.POST.getlist('dpairport')[i]
            airline['dep_date'] = date_for_db_formatter(request.POST.getlist('ddate')[i])
            airline['arr_airport'] = request.POST.getlist('arrairport')[i]
            airline['arr_date'] = date_for_db_formatter(request.POST.getlist('adate')[i])
            airline['airline_class'] = request.POST.getlist('aclass')[i]
            try:
                airline_id = request.POST.getlist('airline_id')[i]
                Airline.objects.filter(id=airline_id).update(**airline)
            except:
                a_created = Airline.objects.create(**airline)
                print(a_created.__dict__)
                exclude_ariline.append(a_created.id)
        Airline.objects.filter(flight_id=flight_id).exclude(id__in=exclude_ariline).delete()
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
                Passenger.objects.filter(id=passenger_id).update(**passenger)
            except:
                created = Passenger.objects.create(**passenger)
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
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
def car_booking(request, id):
    template = 'templates/car_booking.html'
    context = dict()
    context['name'] = id
    return render(request, template, context)


@csrf_exempt
@login_required(login_url='/admin/login')
@transaction.atomic
def booking_error(request):
    template = 'templates/error.html'
    context = dict()
    context['error_msg'] = 'You must create a booking in order to add a hotel against it,' \
                           ' add airline or passengers first'
    return render(request, template, context)\



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
    return render(request, template, context)