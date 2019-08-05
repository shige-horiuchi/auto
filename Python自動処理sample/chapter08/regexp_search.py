import re

item = {}
pattern = r'(?P<weight>\d+)(?P<unit>k?g)以内\s+(?P<fee>(\d{1,3},?)+)円'

with open('postage.txt') as f:
    for line in f:
        match = re.search(pattern, line)        #←正規表現にマッチするかを調べる
        if match is not None:        #←正規表現にマッチしたらNoneではない
            d = match.groupdict()        #←グループに名前を付けたディクショナリを返す
            weight = int(d['weight'])
            if d['unit'] == 'kg':
                weight = weight * 1000        #←単位がkgのときはグラムに変換
            fee = d['fee'].replace(',', '')        #←3桁区切りのカンマを除去
            item[item_type].update({weight: int(fee)})
        elif line != '\n':
            item_type = line.strip()        #←マッチしないときは郵便物の種類の文字列
            item[item_type] = {}

    print(f"定形郵便物 {item['定形郵便物']}")
    print(f"定形外郵便物 {item['定形外郵便物']}")
    print(f"規格外 {item['規格外']}")
