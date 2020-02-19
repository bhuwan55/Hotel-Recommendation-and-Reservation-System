from django import forms
from django.forms import ModelForm
from .models import Reserve
from phonenumber_field.formfields import PhoneNumberField

class reserveform(ModelForm):
    phone_no = PhoneNumberField(widget=forms.TextInput(
            attrs={
              'class':'form-control',
              # 'placeholder':'+977'
          }
    ))
    check_in = forms.DateField(widget = forms.TextInput( 
      attrs={
        'class':'form-control',
        'placeholder':'yyyy-mm-dd'
     }
     ))

    check_out = forms.DateField(widget = forms.TextInput(
      attrs={
        'class':'form-control',
        'placeholder':'yyyy-mm-dd'
     }))

    no_of_rooms = forms.IntegerField(widget = forms.TextInput(
      attrs={
        'class':'form-control',
     }))

    class Meta:
        model = Reserve
        fields=[
          'check_in','check_out','phone_no','no_of_rooms',
        ]
