from django.http import JsonResponse
from rest_framework import serializers
from base.models import Tickets
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('id','flight_id','costumer_id','createdTime')


    def get_All_Tickets(self,obj):
        res = []
        for i in obj:
            res.append({
                "id":i._id,
                "flight_id":{
                    "id": i.flight_id._id,
                    "airline_company_id":{
                       "airline_company_id": i.flight_id._id,
                       "airline_company_name": i.flight_id.airline_company_id.company_name
                    },
                    "origin_country_id":{
                        "origin_country_id":i.flight_id._id,
                        "origin_country_name":i.flight_id.origin_country_id.country_name
                    },
                    "destination_country_id": {
                        "destination_country_id":i.flight_id._id,
                        "destination_country_name":i.flight_id.destination_country_id
                    },
                    "departure_time": i.flight_id.departure_time,
                    "landing_time":i.flight_id.landing_time
                    },
                    "costumer_id":{
                        "costumer_id":i.flight_id._id,
                        "costumer_name":i.costumer_id.first_name,
                    },
                    "createdTime":i.createdTime
            }) 
        return res

    def get_Ticket_By_Id(self,id):
        ticket = Tickets.objects.get(_id=id)
        return{
            "id":ticket._id,
            "flight_id":{
                    "id": ticket.flight_id._id,
                    "airline_company_id":{
                       "airline_company_id": ticket.flight_id._id,
                       "airline_company_name": ticket.flight_id.airline_company_id.company_name
                    },
                    "origin_country_id":{
                        "origin_country_id":ticket.flight_id._id,
                        "origin_country_name":ticket.flight_id.origin_country_id.country_name
                    },
                    "destination_country_id": {
                        "destination_country_id":ticket.flight_id._id,
                        "destination_country_name":ticket.flight_id.destination_country_id
                    },
                    "departure_time": ticket.flight_id.departure_time,
                    "landing_time":ticket.flight_id.landing_time
                    },
                    "costumer_id":{
                        "costumer_id":ticket.flight_id._id,
                        "costumer_name":ticket.costumer_id.first_name,
                    },
                        "createdTime":ticket.createdTime
        }           

    def get_tickets_by_customer(self):
            #companies= Airline_Companies.objects.get(_id = id)
            #airline = Flights.objects.get(airline_company_id=id)
            ticket = Tickets.objects.all()
            for i in ticket:
                print(i.costumer_id.first_name)
            
         

   

            #    res.append({
            #        "flight_id":i.flight_id
            #   })
            #return res
