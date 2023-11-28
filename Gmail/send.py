from __future__ import print_function

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    'https://www.googleapis.com/auth/gmail.readonly',
    "https://www.googleapis.com/auth/gmail.compose"
]

SAMPLE = """<div>
    <table border="0" cellpadding="0" cellspacing="0" width="405" style="border-collapse:collapse;width:305pt">

        <colgroup>
            <col width="81" span="5" style="width:61pt">
        </colgroup>
        <tbody>
            <tr height="27" style="height:20pt">
                <td height="27" width="81"
                    style="height:20pt;width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    Meditation</td>
                <td width="81"
                    style="width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    Web Dev</td>
                <td width="81"
                    style="width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    Job Search</td>
                <td width="81"
                    style="border-left:none;width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    Reading</td>
                <td width="81"
                    style="border-left:none;width:61pt;color:black;font-weight:700;text-align:center;vertical-align:middle;border-top:0.5pt solid windowtext;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    Total</td>
            </tr>
            <tr height="21" style="height:16pt">
                <td height="21" width="81"
                    style="height:16pt;width:61pt;color:black;text-align:center;vertical-align:middle;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    4/7</td>
                <td width="81"
                    style="width:61pt;color:black;text-align:center;vertical-align:middle;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    4/7</td>
                <td width="81"
                    style="width:61pt;color:black;text-align:center;vertical-align:middle;border-top:none;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;border-left:none;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    4/7</td>
                <td width="81"
                    style="border-top:none;border-left:none;width:61pt;color:black;text-align:center;vertical-align:middle;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    3/7</td>
                <td width="81"
                    style="border-top:none;border-left:none;width:61pt;color:black;text-align:center;vertical-align:middle;border-right:0.5pt solid windowtext;border-bottom:0.5pt solid windowtext;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-origin:initial;background-clip:initial;padding-top:1px;padding-right:1px;padding-left:1px;font-size:11pt;font-family:Calibri,sans-serif">
                    15/28</td>
            </tr>

        </tbody>
    </table><br>
</div>
"""


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


def gmail_send_message(text = SAMPLE):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # creds, _ = google.auth.default()
    creds = get_creds()

    try:
        service = build('gmail', 'v1', credentials=creds)

        message = MIMEText(text, 'html')
        message['to'] = 'hrrmainland@gmail.com'
        message['from'] = 'hugoreports@gmail.com'
        message['subject'] = 'Automated draft'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


if __name__ == '__main__':
    # gmail_send_message()
    pass
