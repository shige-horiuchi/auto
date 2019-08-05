with open('postage.txt', encoding='utf-8') as f:        #←postage.txtというファイルを開く
    for line in f:        #←1行ずつlineに読み込む
        print(line)
