import pathlib

def show_recursive(path):
    for po in path.iterdir():
        if po.is_dir():
            show_recursive(po)
        elif po.is_file():
            print(po)

path = pathlib.Path('.')
#path = pathlib.Path(r'C:\Users\s.horiuchi\Documents\Python\auto')
show_recursive(path)