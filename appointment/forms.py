# appointment/forms.py
from django import forms
from .models import Appointment


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['speciality', 'date', 'start_time']
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
        }
