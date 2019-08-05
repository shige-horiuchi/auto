with open('postage.txt', encoding='utf-8') as f:
    for line in f:
        text = line.strip()
        if text.startswith('50g'):        #←接頭辞が50gで始まる
            print(text)
        if (text.endswith('郵便物')        #←接尾辞が郵便物または規格外で終わる
            or text.endswith('規格外')):
            print(text)
