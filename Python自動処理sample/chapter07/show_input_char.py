while True:        #←無限に繰り返すループ処理
    text = input(f'何か入力してください。終了するにはqを入力してください: ')
    if text == 'q':
        break        #←ループ処理を抜け出す
    else:
        print(f'入力したのは{text}です。')
