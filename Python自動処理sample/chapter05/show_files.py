import pathlib

path = pathlib.Path('.')        #←カレントフォルダ(".")を指定
for po in path.iterdir():
    if not po.is_dir():        #←フォルダでない場合に表示する
        print(po)
