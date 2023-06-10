from __future__ import print_function
from pprint import pprint

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
id_calendar = '97af92ea5c0ab57ca14db3410ddf5c12e966b87e801f70555bcadc1e9f7c5d17@group.calendar.google.com'
id_new_event = None
service = None

event_body = {
  'summary': 'Google I/O 2023',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2023-06-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2023-06-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
	dt = datetime.datetime(year, month, day, hour-3, minute, 0).isoformat() + 'Z'
	return str(dt)

def create_event(summary: str, location: str, description: str, start_time: str, end_time: str):
    return {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': 'Europe/Moscow',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Europe/Moscow',
            },
            }


def main():

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        
    except HttpError as error:
        print('An error occurred: %s' % error)

def create():
    new_event = create_event('Бровки у Ксюшки', 'Minsk', 'Какое-то описание', convert_to_RFC_datetime(2023,6,12,14,30), convert_to_RFC_datetime(2023,6,12,16,30))
    event = service.events().insert(calendarId=id_calendar, body=new_event).execute()
    return event['id']
    
def remove(eventId: str):
    service.events().delete(calendarId=id_calendar, eventId=eventId).execute()

if __name__ == '__main__':
    main()
