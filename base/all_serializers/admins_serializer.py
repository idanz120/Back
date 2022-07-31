from rest_framework import serializers
from base.models import Administrators,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
    

class Admin_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Administrators
        fields =("id","first_name","last_name","user_id","createdTime")

    def get_All_Admins(self,obj):
        res = []
        for i in obj:
            res.append({
                #"user_id":i.user_id,
                "id": i._id,
                "first_name": i.first_name,
                "last_name": i.last_name,
                "createdTime": i.createdTime,
                "user_id":{
                    "username": i.user_id.username,
                    "email":i.user_id.email
                }
            }) 
        return res

    def get_Admin_By_Id(self,id):
        adm = Administrators.objects.get(_id=id)
        return {
            "id": adm._id,
            "first_name": adm.first_name,
            "last_name": adm.last_name,
            #"user_id": adm.user_id,
            "createdTime": adm.createdTime,
            "user_id":{
                    "username": adm.user_id.username,
                    "email":adm.user_id.email
                }
        }                    
