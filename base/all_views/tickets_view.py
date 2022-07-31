from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from base.all_serializers.tickets_serializer import TicketSerializer
from base.models import Tickets
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST','DELETE','PUT'])
#@permission_classes([IsAuthenticated])
def tickets(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":TicketSerializer().get_Ticket_By_Id(id),
            },safe=False)
        else: 
            airlineObj= Tickets.objects.all()
            print(airlineObj)
            #return JsonResponse({"GET":CountriesObj})
            return JsonResponse({"ALL Tickets":TicketSerializer().get_All_Tickets(airlineObj)},safe=False) #return array as json response
    #country_name,image
    if request.method == 'POST': #method post add new row
        #ticket_id =request.data['_id']
        #print(request.data['_id'])
        Tickets.objects.create()
        return JsonResponse({'Added':'Ticket'})

    if request.method == 'DELETE': #method delete a row
        temp= Tickets.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Tickets.objects.get(_id = id)
        temp.createdTime =request.data['createdTime']
        temp.save()
 
        return JsonResponse({'PUT': id})

@api_view(['GET','POST','DELETE','PUT'])
def tickets_by_customer(request):
    if request.method == 'GET':
        return JsonResponse({
            "Tickets-By-this-Customer:":TicketSerializer().get_tickets_by_customer(),
            },safe=False)        