import pandas as pd

df = pd.read_csv('item_stock_cp932.csv', header=0, encoding='cp932')
print(df['店舗名'])