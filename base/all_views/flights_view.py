from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.airline_comp_serializer import Airline_Comp_Serializer
from base.all_serializers.flights_serializer import FlightsSerializer
from base.models import Flights,Airline_Companies


@api_view(['GET','POST','DELETE','PUT'])
def flights(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":FlightsSerializer().get_Flights_by_id(id),
            },safe=False)
        else: 
            flightObj= Flights.objects.all()
            #return JsonResponse({"GET":CountriesObj})
            return JsonResponse({"ALL Flights":FlightsSerializer().get_All_Flights(flightObj)},safe=False) #return array as json response
    
    # ( user_id,airline_company_id,origin_country_id,destination_country_id,
    #   departure_time,landing_time,remaining_tickets,createdTime )
    if request.method == 'POST': #method post add new row
        Flights.objects.create(tickets=request.data['remaining_tickets'])
        return JsonResponse({'Added':'FLIGHT add' })

    if request.method == 'DELETE': #method delete a row
        temp= Flights.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Flights.objects.get(_id = id)
        temp.remaining_tickets=request.data['remaining_tickets']
        temp.save()
 
        return JsonResponse({'PUT': id})

# Get User by User Name
@api_view(['GET','POST','DELETE','PUT'])
def flights_by_air_companies(request,id):
    if request.method == 'GET':
        if int(id) > -1: #get single product
           
            return JsonResponse({
            "All Flights-By-This-Airline Company":FlightsSerializer().get_flight_by_airline(id),
            },safe=False)
