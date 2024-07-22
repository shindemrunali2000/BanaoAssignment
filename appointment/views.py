# appointment/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.models import User
from google.oauth2 import service_account 
from googleapiclient.discovery import build 
from .google_calendar import create_google_calendar_event
@login_required
def doctor_list(request):
    doctors = User.objects.filter(profile__user_type='doctor')
    return render(request, 'appointment/doctor_list.html', {'doctors': doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.save()
            # create_google_calendar_event(appointment)  # Function to be defined later
            return redirect('appointment_detail', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'appointment/book_appointment.html', {'form': form, 'doctor': doctor})

@login_required
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointment/appointment_detail.html', {'appointment': appointment})