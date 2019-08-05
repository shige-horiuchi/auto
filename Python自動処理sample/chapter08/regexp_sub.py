import re

html = """<p>
<em>re.sub()</em>関数は正規表現パターンにマッチした文字列を任意の文字列で置換します。
<em>count</em>パラメーターを指定することで文字列を置換する回数を指定できます。
</p>"""

print(f'HTMLドキュメント {html}')
print()

pattern = r'<.*?>'        #←<と>に囲まれた任意の最小文字列、または<>にマッチする
result = re.sub(pattern, '', html)        #←マッチした文字列を空文字に置換する(除去)
print(f"正規表現: r'{pattern}'")
print(f'置換後文字列: {result}')

print(f'マッチした文字列のうち、最初の2つのみ置換します')
result = re.sub(pattern, '', html, count=2)        #←countで置換回数を指定する
print(f'置換後文字列: {result}')
