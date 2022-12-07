from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import BookAppointmentModel
from .forms import AppointmentForm
from django.http import HttpResponseRedirect

# Create your views here.

class Home(generic.TemplateView):
    '''
    Displays Home Page
    '''
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "custom-red",
            }
        )

class BookAppointment(CreateView):
    '''
    After submitting the form the user will be redirected
    to the manage my bookings page where the request
    will be shown as pending approval
    '''
    template_name = 'appointments.html'
    form_class = AppointmentForm
    model = BookAppointmentModel

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.save()
        messages.success(
            self.request,
            'Your request has been submitted and is awaiting for approval')
        return HttpResponseRedirect('/appointments_manage/')

'''
class ManageAppointments(generic.ListView):
    
    Get the data from the database and displays it
    to the user.
    
    model = BookAppointmentModel
    template_name = manage_appointments
    login_required = True
    paginate_by = 6

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = BookAppointmentModel.objects.all()
        context.update({
            "appointments":appointments,
        })
        return context
'''

class DeleteAppoinment(DeleteView):
    '''
    enable users to delete already booked appointment,
    redirects users to manage booking page
    '''

class EditAppointment(UpdateView):
    '''
    allow users to make changes to the appointment,
    once completed the user get redirected to the 
    manage bookings page
    '''
