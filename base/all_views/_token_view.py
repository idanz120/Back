from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
 
 
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
 
        return token 
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# register
@api_view(['POST'])
def addUser(request):
#user_name=request.data['username']
    User.objects.create_user(username= request.data['username'],
                             email=request.data['email'],
                             password= request.data['password'])
    return JsonResponse({"done":'done'} )    

    #User.objects.create_user(username= 'john',
    #                         email='john@.com',
    #                         password= '123321')
    #return JsonResponse({"done":'done'} )   
