from django.contrib import admin
from .models import Customer,Countries,Administrators,Airline_Companies,Flights,User_Roles,Tickets
 
# Register your models here.
admin.site.register(Customer)
admin.site.register(Countries)
admin.site.register(Administrators)
admin.site.register(Airline_Companies)
admin.site.register(Flights)
admin.site.register(User_Roles)
admin.site.register(Tickets)