import pandas as pd

df = pd.read_csv(r'C:\SuperBOX\work\data\horiuchi\受注（過去）.csv', encoding = 'cp932', header = 0)
syouhin = sum(df['商品金額'])
zyucyuu = sum(df['受注金額'])
# print(f'価格合計： {kakaku}')
print('商品金額合計：', syouhin, '受注金額：', zyucyuu)