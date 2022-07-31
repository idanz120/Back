from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.roles_serializer import User_Roles_Serializer
from base.models import User_Roles
#User_Roles
# ( _id,role_name,createdTime )
@api_view(['GET','POST','DELETE','PUT'])
def roles(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":User_Roles_Serializer().get_Roles_By_Id(id),
            },safe=False)
        else: 
            role= User_Roles.objects.all()
            print(role)
            return JsonResponse({"ALL Roles":User_Roles_Serializer().get_All_Roles(role)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        role_name =request.data['role_name']
        print(request.data['role_name'])
        User_Roles.objects.create( role_name = request.data['role_name'])
        return JsonResponse({'Added':role_name})

    if request.method == 'DELETE': #method delete a row
        temp= User_Roles.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=User_Roles.objects.get(_id = id)
        temp.role_name =request.data['role_name']
        temp.save()
        return JsonResponse({'PUT': id})