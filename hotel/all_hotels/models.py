from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image= models.ImageField(blank=True, null=True, upload_to='category/')

    def __str__(self):
        return self.name
        
class Services(models.Model):
    service = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.service

class Price(models.Model):

    price = models.CharField(max_length=100 , null = True)

    def __str__(self):
        return self.price
choicee = zip(range(1,100), range(1,100))

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/')
    location = models.CharField(max_length=100)
    description = models.TextField()
    service_provide = models.ManyToManyField(Services)
    category = models.ManyToManyField(Category)
    tag = models.CharField(max_length=200)
    price = models.ManyToManyField(Price)
    available_rooms = models.IntegerField(choices=choicee, null=True)

    def __str__(self):
        return self.name

RATE_CHOICES = zip( range(1,6), range(1,6) )

class Rate(models.Model):
    rating = models.IntegerField(choices=RATE_CHOICES)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


choicess = zip ( range(1,100), range(1,100))
class Reserve(models.Model):
    phone_no= PhoneNumberField( null=False, blank=False,)
    no_of_rooms = models.IntegerField(choices=choicess, null=True)
    check_in = models.DateField(blank=False,null=True)
    check_out = models.DateField(blank=False,null=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
