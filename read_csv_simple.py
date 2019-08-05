import pandas as pd

df = pd.read_csv('item_stock.csv', encoding = 'utf-8', header = 0)
# df = pd.read_csv(r'C:\Users\s.horiuchi\Documents\Python\auto\item_stock.csv', encoding = 'utf-8', header = 0)
sales = 0
for row in df.values:
    print(f' - 行： {row}')
    # print(' - 行：', row)
    sales += row[2]
    # print(sales, row[2], row)

print(f'売上数合計：　{sales}')
# print('売上数合計：', sales)