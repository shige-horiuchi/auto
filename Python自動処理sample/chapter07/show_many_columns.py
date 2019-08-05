import pandas as pd

pat = 'display.expand_frame_repr'
pd.set_option(pat, False)        #←1行に含まれる列を改行せずに表示
df = pd.read_csv('e-stat-10102.csv', encoding='utf-8', header=0)
print(df[:3])        #←先頭から3行だけ表示