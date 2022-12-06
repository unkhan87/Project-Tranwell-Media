from . import views
from .views import BookAppointment
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('appointments/', BookAppointment.as_view(), name='appointments')
]