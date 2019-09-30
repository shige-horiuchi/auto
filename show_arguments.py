import sys

length = len(sys.argv)
print(f'引数の数： {length}')
print(f'引数： {sys.argv}')
if length > 1:
    print(f'1番目の引数： {sys.argv[1]}')