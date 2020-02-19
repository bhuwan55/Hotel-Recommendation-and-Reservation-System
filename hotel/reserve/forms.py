from django import forms
from .models import reserve
from phonenumber_field.formfields import PhoneNumberField

class reserveform(forms.ModelForm):
    phone = PhoneNumberField()
    class meta:
        model = reserve
        fields=[
        'phone_no','no_of_rooms','check_in','check_out'
        ]
