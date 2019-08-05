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

now = datetime.now()
events_from = now - timedelta(weeks=1)
events_to = now + timedelta(weeks=1)
results = service.events().list(
    calendarId=CALENDAR_ID,
    timeMin=events_from.astimezone().isoformat(),
    timeMax=events_to.astimezone().isoformat()
).execute()
for event in results['items']:
    print(f'タイトル: {event.get("summary")}')
    print(f'説明: {event.get("description")}')
    print(f'場所: {event.get("location")}')
    print(f'開始: {event.get("start")}')
    print(f'終了: {event.get("end")}')
