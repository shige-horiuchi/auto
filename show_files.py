import pathlib

path = pathlib.Path('.')
#path = pathlib.Path(r'C:\Users\s.horiuchi\Documents\Python\auto')        
for po in path.iterdir():
    if not po.is_dir():
        print(po)