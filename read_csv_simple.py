import pandas as pd

df = pd.read_csv('item_stock.csv', encoding = 'utf-8', header = 0)
sales = 0
for row in df.values:
    # print(f' - 行： {row}')
    print(' - 行：', row)
    sales += row[3]

sales_c = '{:,}'.format(sales)
# print(f'売上数合計： {sales_c}')
print('売上数合計：', sales_c)