import locale
import pandas as pd

encoding = locale.getpreferredencoding()
data = {
    '店舗名': ['代々木上原店', '表参道店', '赤坂店', '日比谷店', '大手町店'],
    '期首在庫数': [100, 500, 800, 300, 700],
    '売上数': [50, 200, 300, 100, 200],
    '仕入数': [100, 1000, 600, 500, 1000],
}
df = pd.DataFrame(data)
df.to_csv('item_stock.tsv', index=False, sep='\t',
          columns=['店舗名', '期首在庫数', '売上数', '仕入数'],
          encoding=encoding)
