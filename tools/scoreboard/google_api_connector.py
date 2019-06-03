from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIAL_FILE = 'credentials/credentials.json'
TOKEN_FILE = 'credentials/token.pickle'


def get_creds():
    """
    Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIAL_FILE, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_sheet_data(spreadsheet_id, range_name):
    service = build('sheets', 'v4', credentials=get_creds())
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=range_name).execute()
    return result.get('values', [])


def set_sheet_data(spreadsheet_id, range_name, values):
    body = {'majorDimension': 'COLUMNS', 'values': values}
    service = build('sheets', 'v4', credentials=get_creds())
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='RAW', body=body).execute()


