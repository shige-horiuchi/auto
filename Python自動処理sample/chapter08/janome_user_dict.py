from janome.tokenizer import Tokenizer

# udic_type, udic_encを指定します。
t = Tokenizer('user_simpledic.csv', udic_type='simpledic', udic_enc='utf8')
text = 'エンゼルス大谷翔平がヤンキース戦に先発出場した。'
for token in t.tokenize(text):
    if token.part_of_speech.find('名詞') >= 0:
        print(token.surface)
