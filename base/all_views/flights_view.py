from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.airline_comp_serializer import Airline_Comp_Serializer
from base.all_serializers.flights_serializer import FlightsSerializer
from base.models import Flights,Airline_Companies
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt



@api_view(['GET','POST','DELETE','PUT'])
def flights(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":FlightsSerializer().get_Flights_by_id(id),
            },safe=False)
        else: 
            flightObj= Flights.objects.all()
            #return JsonResponse({"GET":CountriesObj})
            return JsonResponse({"Flights":FlightsSerializer().get_All_Flights(flightObj)},safe=False) #return array as json response
    
    # ( user_id,airline_company_id,origin_country_id,destination_country_id,
    #   departure_time,landing_time,remaining_tickets,createdTime )
    if request.method == 'POST': #method post add new row
        Flights.objects.create(departure_time=request.data['departure_time'],landing_time=request.data['landing_time'] ,tickets=request.data['remaining_tickets'])
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

#Get flight by parameters

@api_view(['GET','POST','DELETE','PUT'])
@csrf_exempt
def get_flight_by_parameters(request,originId,destinationId,date):
    res=[]
    if request.method == 'GET':
       a= request.data['originId']
       b= request.data["destinationId"]
       c= request.data["date"]
       print(f"{a},{b} {c}")
       #date_obj= datetime.strptime(c,'%m/%d/%y %H:%M:%S.%f') 
       #date_obj=datetime.strptime('2022/08/08 15:47','%Y/%m/%d %H:%M')
       origin= Flights.objects.filter(origin_country_id =a,destination_country_id=b,departure_time=c)
       print(origin)
       res= FlightsSerializer().get_All_Flights(origin)
       print(res)
       return JsonResponse({
                "result": FlightsSerializer().get_All_Flights(origin)
       })
    else:return JsonResponse({ "not":"found"}) 

#FlightsSerializer().get_All_Flights(origin)

@api_view(['POST'])
def showResults(request):
    a= request.query_params.get("fromdate")
    c= request.query_params.get("todate")
    searchResult= Flights.objects.raw('select airline_company_id,origin_country_id,destination_country_id,departure_time,landing_time,remaining_tickets,createdTime from Flights where departure_time between "'+a+'" and "'+c+'" ')
    print(searchResult)
    return JsonResponse({"data":searchResult})