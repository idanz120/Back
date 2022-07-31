# Create your models here.

from msilib import add_data
import timeit
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    phone_no = models.CharField(max_length=50,null=True,blank=True)
    credit_card_no = models.CharField(max_length=50,null=True,blank=True)
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#unicue
    createdTime=models.DateTimeField(auto_now_add=True)


    def __str__(self):
     	return self.first_name

# -----------------------------------------------------------------------------------------------------


class Countries(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    country_name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.country_name

# -----------------------------------------------------------------------------------------------------
class Administrators(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.first_name

# -----------------------------------------------------------------------------------------------------



class Airline_Companies(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    company_name = models.CharField(max_length=50,null=True,blank=True)
    country_id =models.ForeignKey(Countries,on_delete=models.SET_NULL,null=True)
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#Delet This Have Twice
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.company_name

# -----------------------------------------------------------------------------------------------------


class Flights(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    airline_company_id =models.ForeignKey(Airline_Companies,on_delete=models.SET_NULL,null=True)
    origin_country_id =models.ForeignKey(Countries,on_delete=models.SET_NULL,null=True)
    destination_country_id = models.CharField(max_length=50,null=True,blank=True)       #models.ForeignKey(origin_country_id,on_delete=models.SET_NULL,null=True) #make erorr ask eyal
    departure_time=models.TimeField()
    landing_time=models.TimeField()
    remaining_tickets = models.IntegerField(null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.destination_country_id

# -----------------------------------------------------------------------------------------------------

class User_Roles(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    role_name = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.role_name


# -----------------------------------------------------------------------------------------------------

class Tickets(models.Model):
    # dont forget to make those FK uniqu becuse 1 costumer (traveler) can have 1 tiket 
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    flight_id=models.ForeignKey(Flights,on_delete=models.SET_NULL,null=True)#uniqu
    costumer_id =models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)#uniqu
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
