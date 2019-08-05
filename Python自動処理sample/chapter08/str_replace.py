with open('postage.txt', encoding='utf-8') as f:
    total = 0
    for line in f:
        text = line.strip()
        if text.startswith('50g'):
            fees = text.split()
            print(fees)
            fee = fees[1].replace('円', '')        #←円を空文字に置換(取り除く)
            print(fee)
            total = total + int(fee)        #←数字を整数型に変換して加算する
            print(f'合計: {total}')
        if text.endswith('郵便物') or text.endswith('規格外'):
            print(text)
