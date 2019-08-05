import pathlib

path = pathlib.Path('.')
for po in path.iterdir():
    if po.match('*.py') or po.match('*.PY'):        #←拡張子が.pyと.PYをフィルター
        print(po)
