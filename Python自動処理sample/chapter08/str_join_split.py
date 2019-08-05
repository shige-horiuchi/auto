with open('postage.txt', encoding='utf-8') as f:
    for line in f:
        text = line.strip()
        if text.startswith('50g'):
            fees = text.split()        #←空白文字で分割する
            print(fees)
            fees.append('手紙')        #←分割したリストに'手紙'という文字列を追加する
            print(fees)
            text2 = '::'.join(fees)        #←'::'を区切り文字として文字列を結合する
            print(text2)
        if text.endswith('郵便物') or text.endswith('規格外'):
            print(text)
