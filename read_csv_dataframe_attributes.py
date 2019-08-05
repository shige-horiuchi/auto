import pandas as pd

# df = pd.read_csv('item_stock.csv', encoding = 'utf-8', header = 0)
df = pd.read_csv(r'C:\Users\s.horiuchi\Documents\Python\auto\item_stock.csv', encoding = 'utf-8', header = 0)
print ('df')
print(df)

print()

print('df.T')
print(df.T)

print()

print('df.shape')
print(df.shape)

print()

print('df.values')
print(df.values)

print()

print("df['売上数']")
print(df['売上数'])