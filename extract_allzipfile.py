import zipfile

with zipfile.ZipFile(r'C:\Users\s.horiuchi\Desktop\test\test.zip', 'r') as zf:
    zf.extractall(r'C:\Users\s.horiuchi\Desktop\test\extract')