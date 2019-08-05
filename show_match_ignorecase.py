import pathlib

path = pathlib.Path('.')
# path = pathlib.Path(r'C:\Users\s.horiuchi\Documents\Python\auto')
for po in path.iterdir():
    if po.match('*.py') or po.match('*.PY'):
        print(po)