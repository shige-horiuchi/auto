import locale
import pandas as pd

encoding = locale.getpreferredencoding()
df = pd.read_csv('item_stock.csv', encoding='utf-8', header=0)
df['期末在庫数'] = df['期首在庫数'] + df['仕入数'] - df['売上数']
df.to_csv('item_stock_add_column.csv', index=False,
          columns=['店舗名', '期首在庫数', '売上数', '仕入数', '期末在庫数'],
          encoding=encoding)