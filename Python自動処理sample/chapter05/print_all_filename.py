import zipfile

with zipfile.ZipFile('mydir1.zip', 'r') as zf:        #←読み込みモードでファイルを開く
    for info in zf.infolist():
        print(info.filename)
