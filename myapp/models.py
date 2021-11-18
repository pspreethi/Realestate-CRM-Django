from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
        firstname = models.CharField(max_length = 60)
        lastname = models.CharField(max_length = 60)
        mobile = models.IntegerField(unique = True)
        address = models.CharField(max_length=60,null=True)
        email = models.EmailField(unique = True)
        gender = models.CharField(max_length = 6)
        dob = models.DateField(null=True)
        city = models.CharField(max_length = 60,null=True)
        state = models.CharField(max_length = 60,null=True)
        occupation = models.CharField(max_length = 60,null=True)
        source = models.CharField(max_length = 60,null=True)
        agent = models.CharField(max_length = 60,null=True)
        follow_up_date = models.DateField(null=True)
        doj = models.DateField(null=True)
        remarks = models.CharField(max_length = 120,blank=True)
        contacted = models.CharField(max_length=10,default="no")

class Property(models.Model):
        banner = models.ImageField(upload_to='banners', default="banner.png")
        property_name = models.CharField(max_length=120, unique=True)
        property_type = models.CharField(max_length=60) 
        area = models.CharField(max_length=60)
        price = models.FloatField()
        no_of_bedrooms = models.PositiveIntegerField()
        no_of_bathrooms = models.PositiveIntegerField()
        city = models.CharField(max_length=20,default='nothing')
        state= models.CharField(max_length=20,default='nothing')


class Review(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
        wished_item = models.ForeignKey(Property,on_delete=models.CASCADE)
        property_name = models.CharField(max_length=120,default='nothing')
        property_type = models.CharField(max_length=60,default='nothing') 
        area = models.CharField(max_length=60,default='nothing')
        price = models.FloatField(default=1)
        no_of_bedrooms = models.PositiveIntegerField(default=1)
        no_of_bathrooms = models.PositiveIntegerField(default=1)
        city = models.CharField(max_length=20,default='nothing')
        state= models.CharField(max_length=20,default='nothing')
        def __str__(self):
                return self.wished_item.title