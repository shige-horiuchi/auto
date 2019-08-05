import csv
import locale
import pandas as pd

encoding = locale.getpreferredencoding()
data = {
    '店舗名': ['代々木\n上原店', '表"参道店', '赤坂店', '日比谷店', '大手町店'],
    '仕入数': [100, '1,000', 600, 500, '1,000'],
}
df = pd.DataFrame(data)
df.to_csv('item_stock_quote_none.csv', quoting=csv.QUOTE_NONE, escapechar="'", encoding=encoding)