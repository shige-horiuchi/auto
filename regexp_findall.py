import re

references = """
 - 結城久子 (2016) 「プログラミング入門」 初心者版
 - 平井重雄 (2014) 「Python入門」 蛇出版
 - 浜田彰三 (2016) 「コンピューター入門」 計算機協会
"""

print(f'参考文献 {references}')

patterns = [
    r'\w+',
    r'「\w+」',
    r'「(\w+)」',
    r'\(2016\)\s「(\w+)」'
]

for pattern in patterns:
    results = re.findall(pattern, references)
    print(f"正規表現 r'{pattern}' => {results}")