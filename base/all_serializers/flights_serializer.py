from base.models import Flights,Airline_Companies
from rest_framework import serializers
#Flights
# ( user_id,airline_company_id,origin_country_id,destination_country_id,
#   departure_time,landing_time,remaining_tickets,createdTime )
class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Flights
        fields= ('id', 'airline_company_id','origin_country_id',
                'destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
                #user_id as option to add also

    def get_All_Flights(self,obj):
        res=[]
        for i in obj:
            res.append({
                "id":i._id,
            #    "user_id":i.user_id,,country_name
                "airline_company_id":{
                    "id": i.airline_company_id._id,
                    "company_name": i.airline_company_id.company_name
                    },
                "origin_country_id":{
                    "id": i.origin_country_id._id,
                    "country_name": i.origin_country_id.country_name

                },
                "destination_country_id":i.destination_country_id,
                "departure_time":i.departure_time,
                "landing_time":i.landing_time,
                "createdTime":i.createdTime,
                "remaining_tickets":i.remaining_tickets

            })
        return res

    def get_Flights_by_id(self,id):
            flight= Flights.objects.get(_id = id)
            return {
            "id": flight._id,
            #"user_id": flight.user_id,
            "airline_company_id": flight.airline_company_id,
            "origin_country_id": flight.origin_country_id,
            "destination_country_id": flight.destination_country_id,
            "departure_time": flight.departure_time,
            "landing_time": flight.landing_time,
            "createdTime": flight.createdTime,
            }  

#    def get_flight_by_airline(self,id):
#            res=[]
#            flight = Flights.objects.filter(airline_company_id =id)
#            print(flight)
#            for i in flight:
#                res.append({
#                    "flight name:":i.destination_country_id
#                })
#            return res


    def get_flight_by_airline(self,id):
            res=[]
            flight = Flights.objects.filter(airline_company_id =id)
            print(flight)
            for i in flight:
                res.append({
                    "airline_company_id":{
                        "company_name":i.airline_company_id.company_name,
                    },
                   "origin_country_id":{
                    "origin_country_id":i.origin_country_id.country_name
                   },
                   "destination_country_id":i.destination_country_id,
                   "departure_time":i.departure_time,
                   "landing_time":i.landing_time,
                   "remaining_tickets":i.remaining_tickets,
                   "createdTime":i.createdTime
                    
                })
            return res
           
         