from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.user_serializer import UserSerializer
from django.contrib.auth.models import User

#User
@api_view(['GET','POST','DELETE','PUT'])
def users(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-User":UserSerializer().get_Users_By_Id(id),
            },safe=False)
        else: 
            adm= User.objects.all()
            print(adm)
            return JsonResponse({"ALL Users":UserSerializer().get_Users(adm)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        username =request.data['username']
        print(request.data['username'])
        User.objects.create( 
        username = request.data['username'],
        email = request.data['email']
        )
        return JsonResponse({'Added':username})

    if request.method == 'DELETE': #method delete a row
        temp= User.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=User.objects.get(_id = id)
        temp.first_name =request.data['username']
        temp.save()
        return JsonResponse({'PUT': id})  

# Get User by User Name
@api_view(['GET','POST','DELETE','PUT'])
def user_by_name(request,name):
    if request.method == 'GET':
        if name==name:
            return JsonResponse({
            "SINGLE-User":UserSerializer().get_user_by_username(name),
            },safe=False)
      