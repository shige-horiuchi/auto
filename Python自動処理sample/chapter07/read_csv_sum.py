import pandas as pd        #←pandas を pd と別名にすることでタイプ数や冗長性を削減

df = pd.read_csv('item_stock.csv', encoding='utf-8', header=0)        #←先頭行がヘッダー行
sales = sum(df['売上数'])
print(f'売上数合計: {sales}')