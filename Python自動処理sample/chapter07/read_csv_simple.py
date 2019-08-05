import pandas as pd

df = pd.read_csv('item_stock.csv', encoding='utf-8', header=0)
sales = 0
for row in df.values:
    print(f' - 行: {row}')
    sales += row[2]        #←売上数は3番目の列
print(f'売上数合計: {sales}')