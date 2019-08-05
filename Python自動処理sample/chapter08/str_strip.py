with open('postage.txt', encoding='utf-8') as f:
    for line in f:
        text = line.strip()        #←改行文字を取り除く
        print(text)
