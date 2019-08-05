SCOPES = ['https://www.googleapis.com/auth/calendar']
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
creds = prepare_credentials()
service = build('calendar', 'v3', credentials=creds)

event_start = datetime(2019, 1, 1, 12, 0)
event_end = event_start + timedelta(hours=1)
# 予定の内容を準備します
event_body = {
  'summary': '予定のタイトル',
  'description': '予定の詳細な説明',
  'start': {'dateTime': event_start.astimezone().isoformat()},
  'end': {'dateTime': event_end.astimezone().isoformat()},
  'location': 'イベントの場所'
}
# CALENDAR_IDで指定されるカレンダーに予定を追加します。
service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
