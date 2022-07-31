from rest_framework import serializers
from base.models import User_Roles

class User_Roles_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Roles
        fields =("id","role_name","createdTime")


    def get_All_Roles(self,obj):
        res = []
        for i in obj:
            res.append({
                "id":i._id,
                "role_name":i.role_name,
                "createdTime":i.createdTime,
                "user_id":{
                    "username": i.user_id.username,
                    "email":i.user_id.email
                }
            })    
        return res

    def get_Roles_By_Id(self,id):
        role = User_Roles.objects.get(_id=id)
        return {
            "id": role._id,
            "role_name": role.role_name,
            "createdTime": role.createdTime,
            "user_id":{
                    "username": role.user_id.username,
                    "email":role.user_id.email
                }
        }   
