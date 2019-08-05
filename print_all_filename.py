import zipfile

with zipfile.ZipFile(r'C:\Users\s.horiuchi\Desktop\test\test.zip', 'r') as zf:
    for info in zf.infolist():
        print(info.filename)