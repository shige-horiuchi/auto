with open('postage.txt', encoding = 'utf-8') as f:
    for line in f:
        text = line.strip()
        if text.startswith('50g'):
            fees = text.split()
            print(fees)
            fees.append('手紙')
            print(fees)
            text2 = '::'.join(fees)
            print(text2)
        if text.endswith('郵便物') or text.endswith('規格外'):
            print(text)