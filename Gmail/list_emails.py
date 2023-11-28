from __future__ import print_function

import base64
from email.message import EmailMessage

import os.path
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import email

import re

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    'https://www.googleapis.com/auth/gmail.readonly',
    "https://www.googleapis.com/auth/gmail.compose"
]


def extract_tbody(text):
    start_index = text.index("<table")
    end_tag = "/table>"
    end_index = text.index(end_tag) + len(end_tag)
    return text[start_index: end_index]


def get_tds(html):
    output = []
    for match in re.finditer(r'<td.*td>', html):
        output.append(match.group())
    return output


def strip_style(target_string):
    for match in re.finditer(r'<[^>]*>', target_string):
        target_string = target_string.replace(match.group(), "")
    return target_string


def get_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('Gmail/token.json'):
        creds = Credentials.from_authorized_user_file(
            'Gmail/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Gmail/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('Gmail/token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def list_emails(creds):
    # Set up the Gmail API service
    service = build('gmail', 'v1', credentials=creds)

    try:
        # Call the Gmail API to get a list of emails in the inbox
        messages = service.users().messages().list(
            userId='me', labelIds=['INBOX']).execute()

        if 'messages' in messages:
            print("List of emails in your inbox:")
            for message in messages['messages']:
                msg = service.users().messages().get(
                    userId='me', id=message['id']).execute()
                print(msg["snippet"])
                # print(
                #     f"Subject: {msg['subject']} | From: {msg['from']} | Date: {msg['internalDate']}")
                if input("y for this one, enter otherwise\n") == "y":
                    return msg["id"]
        else:
            print("No emails found in your inbox.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_email_text(creds, email_id):
    # Set up the Gmail API service
    service = build('gmail', 'v1', credentials=creds)

    try:
        # Call the Gmail API to get the email details
        message = service.users().messages().get(
            userId='me', id=email_id, format='raw').execute()

        # Decode the email message from base64
        raw_data = base64.urlsafe_b64decode(
            message['raw'].encode('ASCII')).decode('utf-8')

        # return raw_data

        msg = email.message_from_string(raw_data)

        # Get the email body (HTML format)
        body_html = ''
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                body_html += part.get_payload(decode=True).decode('utf-8')

        return body_html

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    # Replace 'YOUR_ACCESS_TOKEN' with the actual access token you obtained after authentication
    creds = get_creds()
    id = list_emails(creds)
    raw_data = get_email_text(creds, id)
    # body = extract_tbody(raw_data)
    tds = get_tds(raw_data)
    # print(strip_style(body))
    for td in tds:
        print(strip_style(td), "\n")
    # print(raw_data)
