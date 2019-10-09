import zipfile

with zipfile.ZipFile('mydir1.zip', 'r') as zf:
    for info in zf.infolist():
        print(info.filename)