from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = ((0, "Pending"), (1, "Approved"))

class BookAppointmentModel(models.Model):

    '''
    Model shows what fields are created to book an appointment
    for the user.
    '''
    user_title = [
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('miss', 'Miss')
    ]
    title = models.CharField(max_length=5, choices=user_title)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking', null=True)
    name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    appointment_date = models.DateField()
    appointment_time = models.TimeField(default=timezone.now)
    appointment_comments = models.TextField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    admin_decision = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return str(self.name)
