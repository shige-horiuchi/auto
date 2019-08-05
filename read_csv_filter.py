import pandas as pd

df = pd.read_csv('item_stock.csv', encoding = 'utf-8', header = 0)
# df = pd.read_csv(r'C:\Users\s.horiuchi\Documents\Python\auto\item_stock.csv', encoding = 'utf-8', header = 0)
store = {}
for row in df.values:
    if row[2] >= 200:
        store[row[0]] = row[2]
print(f'売上数が200以上の店舗：  {store}')
# print('売上数が200以上の店舗： ', store)