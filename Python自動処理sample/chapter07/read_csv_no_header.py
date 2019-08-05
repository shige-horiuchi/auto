import pandas as pd

df = pd.read_csv('population.csv', encoding='utf-8', header=None, names=['都道府県名','人口','増減'])
print(f"1行目: {df['都道府県名'][0]}, {df['人口'][0]}")
print(f"3行目: {df['都道府県名'][2]}, {df['人口'][2]}")
