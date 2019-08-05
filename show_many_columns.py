import pandas as pd

pat = 'display.expand_frame_repr'
pd.set_option(pat, False)
df = pd.read_csv('e-stat-10102.csv', encoding = 'utf-8', header = 0)
print(df[:3])