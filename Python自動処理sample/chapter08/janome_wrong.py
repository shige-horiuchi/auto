from janome.tokenizer import Tokenizer

t = Tokenizer()
text = 'エンゼルス大谷翔平がヤンキース戦に先発出場した。'
for token in t.tokenize(text):
    if token.part_of_speech.find('名詞') >= 0:
        print(token.surface)
