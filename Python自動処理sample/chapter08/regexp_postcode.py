import re

text = input(f'郵便番号を入力してください: ')
match = re.search(r'\d{3}-\d{2,4}', text)        #←正規表現にマッチするかを調べる
if match is not None:        #←matchがNoneかどうかで正規表現にマッチしたかどうかがわかる
    postcode = match.group(0)        #←マッチした最初のグループの文字列を取得する
    print(f'{postcode} は正しい郵便番号のフォーマットです')
else:
    print(f'{text} は正しい郵便番号のフォーマットではありません')
