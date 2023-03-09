from django.db import models
from django.contrib.auth.models import User,AbstractUser
from authentication.models import CustomUser

STATE_CHOICES = (
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh' ,' Andhra Pradesh'),
    ('Arunachal Pradesh' , 'Arunachal Pradesh'),
    ('Assam' ,'Assam'),
    ('Bihar' ,'Bihar'),
    ('Chandigarh' , 'Chandigarh'),
    ('Chattisgarh' , 'Chattisgarh'),
    ('Dadra &Nagar Haveli' ,' Dadra &Nagar Haveli'),
    ('Daman and Diu' ,' Daman and Diu'),
    ('Delhi' , 'Delhi'),
    ('Goa' , 'Goa'),
    ("Gujrat" , 'Gujrat') ,
    ('Haryana' , 'Haryana'),
    ('Himachal Pradesh' ,'Himachal Pradesh'),
    ('Jammu & Kashmir' ,'Jammu & Kashmir'),
    ('Jharkhand' , 'Jharkhand'),
    ('Karnataka' , 'Karnataka'),
    ('Kerala' , 'Kerala'),
    ('Lakshyadweep' , 'Lakshyadweep'),
    ('Madhya Pradesh' , 'Madhya Pradesh'),
    ('Maharashtra' , 'Maharashtra'),
    ('Manipur' , 'Manipur'),
    ('Meghalaya' , 'Meghalaya'),
    ('Mizoram' , 'Mizoram'),
    ('Nagaland' , 'Nagaland'),
    ('Odisha' , 'Odisha'),
    ('Puducherry' , 'Puducherry'),
    ('Punjab' , 'Punjab'),
    ('Rajasthan' , 'Rajasthan'),
    ('Sikkim' , 'Sikkim'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana' ,'Telangana'),
    ('Tripura' , 'Tripura'),
    ('Uttrakhand' , 'Uttrakhand'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ("West Bengal" , 'West Bengal'),
)

class Seller(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seller_name=models.CharField(max_length=100)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return str(self.id)







