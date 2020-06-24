# HOW TO USE
# from shacoof.gmailUtil import create_message, send_message, init
# service = init()
# msgJSON = create_message('sharon.cohenofir@trilogy.com','sharon.cohenofir@trilogy.com;shacoof@gmail.com','test-xx','message body xx')
# msg2 = send_message(service,'me',msgJSON)


# https://blog.mailtrap.io/send-emails-with-gmail-api/
# https://developers.google.com/gmail/api/guides/sending#python
from __future__ import print_function
import pickle
import os.path
import base64
from googleapiclient import errors
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def create_message(sender, to, subject, message_text):
#  message = MIMEText(message_text)
  message = MIMEMultipart("alternative", None, [MIMEText(message_text,'html')])
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
  return {
    'raw': raw_message.decode("utf-8")
  }

def send_message(service, user_id, messageJSON):
  try:
    message = service.users().messages().send(userId=user_id, body=messageJSON).execute()
    print('Message Id: %s' % message['id'])
    return message
  except Exception as e:
    print('An error occurred: %s' % e)
    return None

def init():
  creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)

  service = build('gmail', 'v1', credentials=creds)
  return service

if __name__ == '__main__':
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    service = init()
    msgJSON = create_message('sharon.cohenofir@trilogy.com','sharon.cohenofir@trilogy.com;shacoof@gmail.com','test2','message body2')
    msg = send_message(service,'me',msgJSON)
    print('the end')
