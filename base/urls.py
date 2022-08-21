
from base.all_views import customers_view, roles_view, admins_view
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from base.all_views._token_view import MyTokenObtainPairView
from . import views
from .all_views import _token_view
from django.urls import path
from .all_views import admins_view
from .all_views import customers_view
from .all_views import countries_view
from .all_views import airline_comp_view
from .all_views import flights_view
from.all_views import roles_view
from.all_views import tickets_view
from.all_views import user_view

urlpatterns = [
    #Anonimus
    path('', views.index),
    #Cusomers
    path('customers/', customers_view.customers),
    path('customers_by_user/<name>', customers_view.customer_by_username),
    path('customers/<id>', customers_view.customers),
    path('customers_tickets/<id>', customers_view.my_tickets),
    #Countries
    path('countries/', countries_view.countries),
    path('countries/<id>', countries_view.countries),
    path('countryname/<name>', countries_view.countries_name),
    #Airline Companies
    path('airline_companies/', airline_comp_view.airline_companies),
    path('airline_companies/<id>', airline_comp_view.airline_companies),
    #Flights
    path('flightsTEST/<id>', flights_view.showResults),
    path('flights_by_airline/<id>',flights_view.flights_by_air_companies),
    path('flights/', flights_view.flights),
    path('flights/<id>', flights_view.flights),
    path('flight_by_param/<originId><destinationId><date>', flights_view.get_flight_by_parameters),
    #Ticket
    path('tickets/', tickets_view.tickets),
    path('tickets/<id>', tickets_view.tickets),
    path('tickets_by_cust/', tickets_view.tickets_by_customer),
    #Roles
    path('roles/', roles_view.roles),
    path('roles/<id>', roles_view.roles),
    #Admins
    path('admins/', admins_view.admins),
    path('admins/<id>', admins_view.admins),
    #Rgister
    path('adduser/', _token_view.addUser),
    #User
    path('getusers/', user_view.users),
    path('getusers/<id>', user_view.users),
    path('get_user_by_username/<name>', user_view.user_by_name),
    # Login
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
