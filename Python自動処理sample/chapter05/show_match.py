import pathlib

path = pathlib.Path('.')
for po in path.iterdir():
    if po.match('*.py'):        #←拡張子が.pyのファイルのみをフィルター
        print(po)
