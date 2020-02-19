from django.db import models
from all_hotels.models import Hotel
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Cancel_request(models.Model):
    email = models.EmailField(null = False, blank = False)
    phone_no= PhoneNumberField( null=False, blank=False,)
    message = models.TextField(null=True, blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
