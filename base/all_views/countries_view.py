from django.http import JsonResponse
from pytz import country_names
from rest_framework.decorators import api_view
from base.models import Countries
#from base.all_serializers import CountriesSerializer
from base.all_serializers.countries_serializer import CountriesSerializer
#Countries Crud
# ('id','country_name','image')
@api_view(['GET','POST','DELETE','PUT'])
def countries(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":CountriesSerializer().get_Countries_by_id(id),
            },safe=False)
        else: 
            CountriesObj= Countries.objects.all()
            print(CountriesObj)
            #return JsonResponse({"GET":CountriesObj})
            return JsonResponse({"countries":CountriesSerializer().get_Countries(CountriesObj)},safe=False) #return array as json response
    #country_name,image
    if request.method == 'POST': #method post add new row
        country_name =request.data['country_name']
        print(request.data['country_name'])
        Countries.objects.create(country_name=request.data['country_name'] ,image=request.data['image'])
        return JsonResponse({'Added':country_name})

    if request.method == 'DELETE': #method delete a row
        temp= Countries.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Countries.objects.get(_id = id)
        temp.country_name =request.data['country_name']
        temp.image =request.data['image']
        temp.save()
 
        return JsonResponse({'PUT': id})

#Get country by name
@api_view(['GET','POST','DELETE','PUT'])
def countries_name(request,name):
    if request.method == 'GET':
        if name==name:
            return JsonResponse({
            "SINGLE-country":CountriesSerializer().get_Countries_name(name),
            },safe=False)
        else: return JsonResponse({"Country":"not Found"})

      

