SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
def prepare_credentials():
    # 'token.pickle'というファイルに認証結果を保存しておき
    # 認証がすでにされている場合はスキップする、という処理を行なっています。
    import pickle
    import os.path
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = service_account.Credentials.from_service_account_file(
                    'credentials.json', scopes=SCOPES)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

from googleapiclient.discovery import build

SPREADSHEET_ID = '<<スプレッドシートID>>'
creds = prepare_credentials()
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
info = sheet.get(spreadsheetId=SPREADSHEET_ID).execute()
print(f'スプレッドシートID: {info["spreadsheetId"]}')
print(f'タイトル: {info["properties"]["title"]}')
print('シート一覧')
for sh in info["sheets"]:
    print(f'  シートID: {sh["properties"]["sheetId"]} シート名: {sh["properties"]["title"]}')
