import zipfile

with zipfile.ZipFile('mydir1.zip', 'r') as zf:
    zf.extractall('extract_dir')