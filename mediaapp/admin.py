from django.contrib import admin
from .models import BookAppointmentModel

@admin.register(BookAppointmentModel)
class AppointmentAdmin(admin.ModelAdmin):
    '''
    customising admin page so its easier for the
    admin to manage appointments
    '''
    list_filter = (
        'status', 'appointment_date', 'appointment_time', 
        'admin_decision')
    list_display = (
        'title', 'name', 'company_name', 'email', 'created_date', 'appointment_date', 
        'appointment_time', 'status')
    search_fields = ['name']
    actions = ['approve_appointment']

    def approve_appointment(self, request, queryset):
        queryset.update(approved=True)

