import sys
import unicodedata

import pandas as pd


def get_east_asian_width(text):
    """
    >>> get_east_asian_width('text')
    4
    >>> get_east_asian_width('文字')
    4
    """
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in ('F', 'W', 'A'):
            width += 2
        else:
            width += 1
    return width


def generate_spaces(text_width, max_width):
    """
    >>> generate_spaces(4, 6)
    '  '
    """
    return ' ' * (max_width - text_width)


def usage():
    if len(sys.argv) < 3:
        print(f'{__file__} の後にCSVファイルと表示する列番号を指定してください')
        print(f'実行例:')
        print(f'  python {__file__} e-stat-10102.csv 1,3,22,23,24')
        sys.exit(0)



def main():
    df = pd.read_csv(sys.argv[1], encoding='utf-8', header=0)
    column_length = [get_east_asian_width(c) for c in df.columns]

    column_numbers = sys.argv[2].split(',')        #←文字列をカンマ区切りでリスト化
    target_col_numbers = [int(i) for i in column_numbers]
    max_column_length = max(column_length[i] for i in target_col_numbers)

    for line, row in enumerate(df.values, 1):
        print(f'\n##### {line}行目のデータ')

        for i, (column, value) in enumerate(zip(df.columns, row)):
            if i not in target_col_numbers:        #←列番号のチェック
                continue        #←次のループ処理へ移る

            spaces = generate_spaces(column_length[i], max_column_length)
            print(f'{i:0>3}: {column}{spaces}: {value}')

        print(f'#' * 72)
        char = input(f'次行はエンターを、終了はqを入力してください: ')
        if char == 'q':
            break


if __name__ == '__main__':
    usage()
    main()
