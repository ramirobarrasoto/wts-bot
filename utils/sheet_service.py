import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet():
    scope = ["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Housekeeping Reports").sheet1
    return sheet

def append_to_sheet(values):
    sheet = get_sheet()
    sheet.append_row(values)
