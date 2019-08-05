import zipfile

with zipfile.ZipFile(r'C:\Users\s.horiuchi\Desktop\test\test.zip', 'a', compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(r'C:\Users\s.horiuchi\Desktop\test\test_c.csv')