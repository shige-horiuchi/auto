import zipfile

with zipfile.ZipFile(r'C:\Users\s.horiuchi\Desktop\test\test.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(r'C:\Users\s.horiuchi\Desktop\test\test_a.csv')
    zf.write(r'C:\Users\s.horiuchi\Desktop\test\test_b.csv')