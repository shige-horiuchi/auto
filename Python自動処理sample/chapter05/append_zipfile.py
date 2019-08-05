import zipfile

with zipfile.ZipFile('mydir1.zip', 'a') as zf:        #←追記モードでファイルを開く
    zf.write('test3.txt')
