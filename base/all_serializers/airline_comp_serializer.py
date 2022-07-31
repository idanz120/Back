from base.models import Flights
from base.models import Airline_Companies,User,Countries
from rest_framework import serializers




#( _id,company_name,country_id,user_id,createdTime )
class Airline_Comp_Serializer(serializers.ModelSerializer):
    class Meta:
        model =Airline_Companies
        fields= ('id','company_name','country_id','user_id','createdTime')        

    def get_Airline_Comp_by_id(self,id):
            companies= Airline_Companies.objects.get(_id = id)
            return {
            "id": companies._id,
            "company_name": companies.company_name,
            "country_id":{ 
                "country_name":companies.country_id.country_name
            },
            "createdTime": companies.createdTime,
             "user_id":{
                    "username": companies.user_id.username,
                    "email":companies.user_id.email
                }
            }

    def get_Airline_Comp(self,obj):
        res =[]
        for i in obj:
            res.append({
            "id":i._id,
            "company_name":i.company_name,
            "country_id":{ 
                "country_name":i.country_id.country_name
                
            },
            "createdTime":i.createdTime,
            "user_id":{
                   "username": i.user_id.username,
                   "email":i.user_id.email
                }})
        return res


       
       
 
        
