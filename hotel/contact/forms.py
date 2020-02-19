from django import forms
from django.forms import ModelForm
from .models import Cancel_request
from phonenumber_field.formfields import PhoneNumberField

class contactform(ModelForm):
    email = forms.EmailField(widget = forms.TextInput( attrs={
     'class':'form-control',
     'placeholder':'xyz@abc.com'
    }))
    phone_no = PhoneNumberField(widget=forms.TextInput( attrs={
     'class':'form-control',
     'placeholder':'+977'
     }))
    message = forms.CharField(widget=forms.TextInput( attrs={
     'class':'form-control',
     'placeholder':'your message here'
     }))
    class Meta:
        model = Cancel_request
        fields=[
          'email','phone_no','message','hotel',
        ]
