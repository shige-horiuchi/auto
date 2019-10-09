import zipfile

with zipfile.ZipFile('mydir1.zip', 'a') as zf:
    zf.write('test3.txt')