from django import forms
from django.forms import ModelForm
from .widgets import TimePickerInput
from .models import Salon, Booking, Service
from django import forms


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['numberofpeople', 'date']
        widgets ={
            'date' : TimePickerInput(),
        }

class AddSalonForm(ModelForm):
    class Meta:
        model = Salon
        fields = ['salonname', 'address', 'starttime', 'closetime']

        widgets = {
            'starttime' : TimePickerInput(),
            'closetime' : TimePickerInput(),
        }

class AddServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['servicename', 'description', 'price']