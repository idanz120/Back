#Airline_Companies Crud
from base.models import Airline_Companies
from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.airline_comp_serializer import Airline_Comp_Serializer

#( _id,company_name,country_id,user_id,createdTime)
@api_view(['GET','POST','DELETE','PUT'])
def airline_companies(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":Airline_Comp_Serializer().get_Airline_Comp_by_id(id),
            },safe=False)
        else: 
            airlineObj= Airline_Companies.objects.all()
            print(airlineObj)
            #return JsonResponse({"GET":CountriesObj})
            return JsonResponse({"ALL Airline-Companies":Airline_Comp_Serializer().get_Airline_Comp(airlineObj)},safe=False) #return array as json response
    #country_name,image
    if request.method == 'POST': #method post add new row
        company_name =request.data['company_name']
        print(request.data['company_name'])
        Airline_Companies.objects.create(company_name=request.data['company_name'])
        return JsonResponse({'Added':company_name})

    if request.method == 'DELETE': #method delete a row
        temp= Airline_Companies.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Airline_Companies.objects.get(_id = id)
        temp.company_name =request.data['company_name']
        temp.save()
 
        return JsonResponse({'PUT': id})



