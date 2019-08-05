with open('postage.txt', encoding = 'utf-8') as f:
    for line in f:
        text = line.strip()
        if (text.endswith('郵便物') or text.endswith('規格外')):
            print(text)
        if text.startswith('50g'):
            print(text)
        