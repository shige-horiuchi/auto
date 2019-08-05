# スプレッドシートとカレンダー双方へアクセスすることを宣言します
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/spreadsheets'
]
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
from datetime import datetime, timedelta

CALENDAR_ID = '<<カレンダーID>>'
SPREADSHEET_ID = '1fcw3hX6iB0c_T53rgnaJD8bpUboxH2rO83SyJo-y5K0' #<<スプレッドシートID>>'
creds = prepare_credentials()
calendar_service = build('calendar', 'v3', credentials=creds)
sheets_service = build('sheets', 'v4', credentials=creds)
sheet = sheets_service.spreadsheets()

# ---- まずはカレンダーから予定を取得します ------
now = datetime.now()
events_from = now - timedelta(weeks=1)
events_to = now + timedelta(weeks=1)
results = calendar_service.events().list(
    calendarId=CALENDAR_ID,
    timeMin=events_from.astimezone().isoformat(),
    timeMax=events_to.astimezone().isoformat()
).execute()

# ---- 予定のデータを、スプレッドシートのデータに変換します ------

# Calendar APIの返す時刻オブジェクトを
# Sheets APIに'USER_ENTERED'として渡すための形式に変換
def convert_timestamp(calendar_timestamp):
    if 'date' in calendar_timestamp:
        # 終日イベントの場合の処理
        # 'date'フィールドをPythonの`datetime`オブジェクトに変換
        timestamp = datetime.fromisoformat(calendar_timestamp['date'])
    elif 'dateTime' in calendar_timestamp:
        # 通常イベントの場合の処理
        # 'dateTime'フィールドをPythonの`datetime`オブジェクトに変換
        timestamp = datetime.fromisoformat(calendar_timestamp['dateTime'])
    else:
        return '不明なフォーマット'
    # '2019/02/02 17:58:34' のような形式に変換します
    return timestamp.strftime('%Y/%m/%d %H:%M:%S')

# 書き込むデータを準備します
event_rows = []
for event in results['items']:
    event_rows.append([
      event.get("summary"),
      convert_timestamp(event["start"]),
      convert_timestamp(event["end"]),
      event.get("location", ''),
      event.get("description", '')
    ])

# ---- 最後にスプレッドシートに書き込みます ------
updating_data = {
  'values': event_rows
}
sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    valueInputOption='USER_ENTERED',
    range='A1',
    body=updating_data).execute()
