filename = 'print.csv'
print(f'{filename} ファイルに書き込みます')
with open(filename, 'w') as f:
    print(1, 2, 3, sep=',', file=f, flush=True)
    print(4, 5, 6, sep=',', file=f, flush=True)
    print(7, 8, 9, sep=',', file=f, flush=True)
