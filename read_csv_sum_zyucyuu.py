import pandas as pd

df = pd.read_csv(r'顧客受注.csv', encoding = 'CP932', header = 0)
# df = pd.read_csv(r'C:\SuperBOX\work\data\horiuchi\受注（過去）.csv', encoding = 'CP932', header = 0)
syouhin = sum(df['商品金額'])
zyucyuu = sum(df['受注金額'])

sagaku = syouhin - zyucyuu

syouhin_c = '{:,}'.format(syouhin)
zyucyuu_c = '{:,}'.format(zyucyuu)
sagaku_c = '{:,}'.format(sagaku)

# print(f'商品金額　合計： {syouhin}', f'受注金額　合計： {zyucyuu}')
print('商品金額 合計：', syouhin_c, '受注金額：', zyucyuu_c, '差額：', sagaku_c)