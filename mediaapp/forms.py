'''
Appointment Booking Form
'''
import datetime
from django import forms
from .models import BookAppointmentModel
# from bootstrap_datepicker_plus.widgets import DatePickerInput

# for users to get the current date
CURRENT_DATE = str(datetime.date.today())

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = BookAppointmentModel
        fields = ('title', 'name', 'company_name', 'email', 
        'appointment_date', 'appointment_time', 'appointment_comments')

        labels = {
            'appointment_date': 'Appointment Date',
            'appointment_time' : 'Appointment Time',
            'appointment_comments' : 'Message',
            'company_name' : 'Company Name'
        }

        '''
        widgets = {
            'appointment_date': DatePickerInput(
                 options={
                    "format": "DD/MM/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    'minDate': CURRENT_DATE,
                    }
            )
        }
        '''

    