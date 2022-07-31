from base.models import Tickets
from base.models import Customer,User
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields= ('id','first_name','last_name', 'address', 'phone_no', 'credit_card_no', 'user_id', 'createdTime')
    
    def get_Customers_name(self,obj):
        return obj.desc
         
    def get_Customers(self,objec):
        res=[]
        for i in objec:
            res.append({
                
            "id": i._id,
            "first_name": i.first_name,
            "last_name": i.last_name,
            "address": i.address,
            "phone_no": i.phone_no,
            "credit_card_no": i.credit_card_no,
            "user_id":(i.user_id_id), #!!!----not serelayzable whithout "str"----!!!!  make sure you fix it
            "createdTime": i.createdTime
            },)   
        return res


    def get_Customers_by_id(self,id):
        product= Customer.objects.get(_id = id)
        return {
            "id": product._id,
            "first_name": product.first_name, 
            "last_name": product.last_name,
            "address": product.address,
          
        }

    def get_Customer_By_UserName(self,name):
        try:
            names = Customer.objects.get(first_name = name)
        except:return {"Not" :"Found"}    
        print(names)
        return{
                "id":names._id,
                "first_name":names.first_name,
                "last_name":names.last_name,
                }    

                
    def get_my_tickets(self,id): 
        ticket = Tickets.objects.get(costumer_id =id)
        print(ticket)
        return{
            "user_id":{
                "user_id":ticket._id,
                "username":ticket.user_id.username
            },
            "flight_id":{
                "flight_id":ticket.flight_id._id,
                "destination_country_id":ticket.flight_id.destination_country_id
                
            },
            "costumer_id":{
                "costumer_id":ticket.costumer_id._id,
                "first_name":ticket.costumer_id.first_name
            },
            "createdTime":ticket.createdTime

        }
