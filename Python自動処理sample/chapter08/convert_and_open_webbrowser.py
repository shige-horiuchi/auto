import locale
import os
import webbrowser

import markdown2

md_file = 'sample1.md'
html_file = 'sample1_from_module.html'
html_enc = locale.getpreferredencoding()

with open(md_file, 'r', encoding='utf-8') as md, open(html_file, 'w', encoding=html_enc) as html:
    md_format = md.read()        #← markdownフォーマットのテキストを読み込む
    html_format = markdown2.markdown(md_format)        #← フォーマット変換
    html.write(html_format)        #← htmlに変換したテキストを書き込む

current_dir = os.getcwd()
uri = f'file://{current_dir}/{html_file}'
webbrowser.open_new_tab(uri)        #← Webブラウザで開く
