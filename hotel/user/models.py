from django.db import models
from all_hotels.models import Hotel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


# Create your models here.
class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
