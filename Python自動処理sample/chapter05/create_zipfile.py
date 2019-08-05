import zipfile

with zipfile.ZipFile('mydir1.zip', 'w') as zf:        #←書き込みモードでファイルを開く
    zf.write('mydir1/test1.txt')        #← 圧縮したいファイルのパスを指定する
    zf.write('mydir1/test2.txt')
