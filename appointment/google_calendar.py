# appointment/google_calendar.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Define the scopes and service account file path
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = "E:\\Mrunali\\service-account-file.json"

# Create a credentials object from the service account file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the calendar service
service = build('calendar', 'v3', credentials=credentials)

def create_google_calendar_event(appointment):
    appointment_start = datetime.combine(appointment.date, appointment.start_time)
    appointment_end = appointment_start + timedelta(minutes=45)

    event = {
        'summary': f'Appointment with {appointment.patient.get_full_name()}',
        'start': {
            # 'dateTime': datetime.combine(appointment.date, appointment.start_time).isoformat(),
            'dateTime': appointment_start.isoformat(),
            'timeZone': 'UTC',
        },
        'end': {
            # 'dateTime': datetime.combine(appointment.date, appointment.end_time).isoformat(),
            'dateTime': appointment_end.isoformat(),
            'timeZone': 'UTC',
        },
        'attendees': [
            {'email': appointment.doctor.email},
        ],
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')
