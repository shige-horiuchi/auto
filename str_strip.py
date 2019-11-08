with open('postage.txt', encoding = 'utf-8') as f:
    for line in f:
        text = line.strip()
        print(text)