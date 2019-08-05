import zipfile

with zipfile.ZipFile('mydir1.zip', 'r') as zf:        #←読み込みモードでファイルを開く
    zf.extractall('extract_dir')
