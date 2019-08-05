import re

text = input('郵便番号を入力して下さい：　')
match = re.search(r'\d{3}-\d{2,4}', text)
print(match)
if match is not None:
    postcode = match.group(0)
    print(f'{postcode} は正しい郵便番号のフォーマットです')
else:
    print(f'{text} は正しい郵便番号のフォーマットではありません')