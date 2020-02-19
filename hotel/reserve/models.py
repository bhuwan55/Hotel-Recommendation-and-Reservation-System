from django.db import models
from django.contrib.auth.models import User
from all_hotels.models import Hotel
from phonenumber_field.modelfields import PhoneNumberField

class reserve(models.Model):
    phone_no = PhoneNumberField(null=False, blank=False, unique=True)
    no_of_rooms = models.IntegerField(blank=True, null=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
