import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1jzL9A2OTT7oweDltR0ThirMLhMUMOgxFrwCp0dBG87E"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.credentials = None
        self.set_credentials()
        self.destination_data = None

        self.service = build("sheets", 'v4', credentials=self.credentials)
        self.sheets = self.service.spreadsheets()
    def set_credentials(self):
        if os.path.exists("token.json"):
            self.credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                self.credentials = flow.run_local_server(port=0)
            with open("token.json", 'w') as token:
                token.write(self.credentials.to_json())

    def get_destination_data(self):

        result = self.sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="prices!A2:C11").execute()
        self.destination_data = result.get('values')
        # result2 = self.sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="users!A1:C1").execute()
        # print(result2)
        return self.destination_data

    def set_destination_data(self, destination, index, column):

        row = ''
        destination_index = -1

        match column:
                case 'IATA':
                    row = 'B'
                    destination_index= 1
                    self.sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"prices!{row}{index + 2}",
                                                valueInputOption="USER_ENTERED",
                                                body={"values": [[f"{destination[destination_index]}"]]}).execute()

                case 'lowest price':
                    row = 'C'
                    destination_index= 2
                    self.sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"prices!{row}{index + 2}",
                            valueInputOption="USER_ENTERED",
                            body={"values": [[f"{destination[destination_index]}"]]}).execute()
                case other:
                    print("No match found")



