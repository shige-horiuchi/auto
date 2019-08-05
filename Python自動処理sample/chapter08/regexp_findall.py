import re

references = """
- 結城久子 (2016) 「プログラミング入門」 初心者出版
- 平井重雄 (2014) 「Python入門」 蛇出版
- 浜田彰三 (2016) 「コンピューター入門」 計算機協会
"""

print(f'参考文献 {references}')

patterns = [
    r'\w+',        #←文字、数字、アンダースコアが1文字以上続く文字列
    r'「\w+」',        #←「と」で囲まれた文字列
    r'「(\w+)」',        #←「と」で囲まれた内部の文字列
    r'\(2016\)\s「(\w+)」',        #←(2016)の後ろに空白があり「と」の内部の文字列
]

for pattern in patterns:
    results = re.findall(pattern, references)
    print(f"正規表現 r'{pattern}' => {results}")
