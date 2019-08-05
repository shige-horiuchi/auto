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
# spreadsheetIdでしていしたスプレッドシートの範囲'A1:C2'を指定して値を取得します
cell_range = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='A1:C2').execute()
print(cell_range.get('values'))
