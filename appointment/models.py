# appointment/models.py
from datetime import datetime, timedelta, time
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='patient_appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_appointments', on_delete=models.CASCADE)
    speciality = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def save(self, *args, **kwargs):
        # Combine the appointment date and start time into a datetime object
        start_datetime = datetime.combine(self.date, self.start_time)
        # Add 45 minutes to the start datetime to get the end datetime
        end_datetime = start_datetime + timedelta(minutes=45)
        # Extract the time part of the end datetime and assign it to end_time
        self.end_time = end_datetime.time()
        super(Appointment, self).save(*args, **kwargs)

    def __str__(self):
        # return f"Appointment with {self.doctor} on {self.date} at {self.start_time}"
        return f'Appointment with Dr. {self.doctor.get_full_name()} on {self.date} at {self.start_time}'
