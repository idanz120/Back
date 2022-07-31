#Customer Crud
# ('id','first_name','last_name', 'address', 'phone_no', 'credit_card_no', 'user_id', 'createdTime')
from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.models import Customer,User
from base.all_serializers.customer_serializer import CustomerSerializer

@api_view(['GET','POST','DELETE','PUT'])
def customers(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Customer":CustomerSerializer().get_Customers_by_id(id),
            },safe=False)

        else: 
            CustomerObj= Customer.objects.all()
            print(CustomerObj)
            return JsonResponse({"ALL-CUSTO":CustomerSerializer().get_Customers(CustomerObj)},safe=False) #return array as json response
  
    if request.method == 'POST': #method post add new row
        first_name =request.data['first_name']
        print(request.data['first_name'])
        Customer.objects.create( 
         first_name=request.data['first_name'] 
        ,last_name=request.data['last_name']
        ,address = request.data['address'],
        phone_no = request.data['phone_no'],
        credit_card_no = request.data['credit_card_no']
        
        )
        return JsonResponse({'POST':first_name})

    if request.method == 'DELETE': #method delete a row
        temp= Customer.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Customer.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})


#Get country by name
@api_view(['GET','POST','DELETE','PUT'])
def customer_by_username(request,name):
    if request.method == 'GET':
        if name==name:
            return JsonResponse({
            "SINGLE-Customer":CustomerSerializer().get_Customer_By_UserName(name),
            },safe=False)

@api_view(['GET','POST','DELETE','PUT'])
def my_tickets(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "Tickets by Customer":CustomerSerializer().get_my_tickets(id),
            },safe=False)              