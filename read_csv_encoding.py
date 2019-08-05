import pandas as pd

df = pd.read_csv('item_stock_cp932.csv', encoding = 'cp932', header = 0)
# df = pd.read_csv(r'C:\Users\s.horiuchi\Documents\Python\auto\item_stock_cp932.csv', encoding = 'cp932', header = 0)

print(df['店舗名'])