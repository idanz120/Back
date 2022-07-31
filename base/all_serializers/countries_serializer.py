#from base.views_countries import countries
from django.http import JsonResponse
from base.models import Countries
from rest_framework import serializers

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Countries
        fields= ('id','country_name','image')
            
    def get_Countries(self,objec):
        res=[]
        for i in objec:
            res.append({
                "id": i._id,
                "country_name": i.country_name,
                "image": str(i.image),
            },)   
        return res


    def get_Countries_by_id(self,id):
        product= Countries.objects.get(_id = id)
        return {
            "id": product._id,
            "country_name": product.country_name,
            "image": str(product.image),
            }

    def get_Countries_name(self,name):
        try:     
            names = Countries.objects.get(country_name = name)
        except:return {"Not" :"Found"} 
        print(names)
        if names:
            return{
                "id":names._id,
                "country_name":names.country_name,
                "image": str(names.image)
                }    