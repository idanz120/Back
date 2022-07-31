from django.http import JsonResponse
from rest_framework.decorators import api_view
#from base.all_serilizers.admins_serializer import Admin_Serializer
from base.all_serializers.admins_serializer import Admin_Serializer
from base.models import Administrators

# Adminstartor
# ( id,first_name,last_name,user_id,createdTime )
@api_view(['GET','POST','DELETE','PUT'])
def admins(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":Admin_Serializer().get_Admin_By_Id(id),
            },safe=False)
        else: 
            adm= Administrators.objects.all()
            print(adm)
            return JsonResponse({"ALL Admins":Admin_Serializer().get_All_Admins(adm)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        first_name =request.data['first_name']
        print(request.data['first_name'])
        Administrators.objects.create( 
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
        )
        return JsonResponse({'Added':first_name})

    if request.method == 'DELETE': #method delete a row
        temp= Administrators.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Administrators.objects.get(_id = id)
        temp.first_name =request.data['first_name']
        temp.last_name =request.data['last_name']
        temp.save()
        return JsonResponse({'PUT': id})  