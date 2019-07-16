"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import landing_page, homepage, flight_booking_view, \
    flight_booking_change_view, flight_delete_view, hotel_booking,\
    booking_error, car_booking, tours_booking, cruise_booking, hotel_delete_view, payment, package, generate_history,\
    history, profit_report, advance_profit_report, supplier_report

urlpatterns = [
    path('', landing_page),
    path('homepage/', homepage),
    path('admin/', admin.site.urls),
    path('flight_booking/', flight_booking_view),
    path('flight_booking/<int:id>/change/', flight_booking_change_view),
    path('flight_booking/<int:booking_id>/<int:flight_id>/delete/', flight_delete_view),
    path('hotel_booking/<int:booking_id>/<int:hotel_id>/delete/', hotel_delete_view),
    path('hotel_booking/<int:id>/change/', hotel_booking),
    path('car_hire/<int:id>/change/', car_booking),
    path('tours/<int:id>/change/', tours_booking),
    path('package/<int:id>/change/', package),
    path('payments/<int:id>/change/', payment),
    path('cruise_hire/<int:id>/change/', cruise_booking),
    path('history/<int:id>/change/', history),
    path('profit_report/', profit_report),
    path('advance_profit_report/', advance_profit_report),
    path('supplier_report/', supplier_report),
    path('hotel_booking/', booking_error),
    path('cruise_hire/', booking_error),
    path('car_hire/', booking_error),
    path('tours/', booking_error),
    path('accounts/', booking_error),
    path('package/', booking_error),
    path('_nested_admin/', include('nested_admin.urls')),

]
admin.site.site_header = "George Travels"
admin.site.site_title = "George Travels Admin Panel"
admin.site.index_title = "Welcome to George Travels Admin Panel"
