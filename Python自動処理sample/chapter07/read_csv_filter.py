import pandas as pd

df = pd.read_csv('item_stock.csv', encoding='utf-8', header=0)
store = {}
for row in df.values:
    if row[2] >= 200:        #←売上数は3番目の列
        store[row[0]] = row[2]        #←店舗名は1番目の列
print(f'売上数が200以上の店舗: {store}')
