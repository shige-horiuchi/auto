import csv        #←quotingを指定するためにcsvモジュールをインポート
import locale
import pandas as pd

encoding = locale.getpreferredencoding()
data = {
    '店舗名': ['代々木\n上原店', '表"参道店', '赤坂店', '日比谷店', '大手町店'],
    '期首在庫数': [100, 500, 800, 300, 700],
    '売上数': [50, 200, 300, 100, 200],
    '仕入数': [100, '1,000', 600, 500, '1,000'],
}
df = pd.DataFrame(data)
df.to_csv('item_stock_quote_minimal.csv', index=False,
          quoting=csv.QUOTE_MINIMAL,
          columns=['店舗名', '期首在庫数', '売上数', '仕入数'],
          encoding=encoding)
df.to_csv('item_stock_quote_all.csv', index=False,
          quoting=csv.QUOTE_ALL,
          columns=['店舗名', '期首在庫数', '売上数', '仕入数'],
          encoding=encoding)
df.to_csv('item_stock_quote_nonnumeric.csv', index=False,
          quoting=csv.QUOTE_NONNUMERIC,
          columns=['店舗名', '期首在庫数', '売上数', '仕入数'],
          encoding=encoding)
