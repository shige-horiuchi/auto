import pathlib

def show_recursive(path):
    for po in path.iterdir():
        if po.is_dir():
            show_recursive(po)        #←ディレクトリなら再帰的にshow_recursive()を呼び出す
        elif po.is_file():
            print(po)        #←ファイルなら表示する

path = pathlib.Path('.')
show_recursive(path)
