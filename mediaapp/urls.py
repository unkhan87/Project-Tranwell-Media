from . import views
from .views import BookAppointment, ManageAppointments, DeleteAppointment, AppointmentUpdate
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('appointments/', BookAppointment.as_view(), name='appointments'),
    path('manage_appointments/', ManageAppointments.as_view(), name='manage_appointment'),
    path('delete/<int:pk>', DeleteAppointment.as_view(), name='delete_appointment'),
    path('update/<int:pk>', AppointmentUpdate.as_view(), name='update_appointment'),
]