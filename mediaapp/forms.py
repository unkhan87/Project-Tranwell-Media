'''
Appointment Booking Form
'''
import datetime
from django import forms
from .models import BookAppointmentModel
# from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
# from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

# for users to get the current date
CURRENT_DATE = str(datetime.date.today())

class DatePicker(forms.DateInput):
        input_type = 'date'

class TimePicker(forms.TimeInput):
        input_type = 'time'

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

        
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_date': DatePicker(attrs={'class': 'form-control'}),
            'appointment_time': TimePicker(attrs={'class': 'form-control'}),
            'appointment_comments': forms.Textarea(attrs={'class': 'form-control'})
        }
        

    