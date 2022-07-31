from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields= ('id','username','last_name','email')

    def get_Users(self,objec):
        res=[]
        for i in objec:
            res.append({
                "id": i.id,
                "username": i.username,
                "email": i.email
            },)   
        return res

    def get_Users_By_Id(self,_id):
            user= User.objects.get(id = _id)
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
                }    

    def get_user_by_username(self,name):
        try:
            names = User.objects.get(username = name)
        except:return {"Not" :"Found"}
        print(names)
        return {
                "id": names.id,
                "username": names.username,
                "email": names.email
                }
                 

#    def get_Customer_By_UserName(self,name):
#        names = Customer.objects.get(first_name = name)
#        print(names)
#        if names:
#            return{
#                "id":names._id,
#                "first_name":names.first_name,
#                "last_name":names.last_name,
#                
#                }                