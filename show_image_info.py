from PIL import Image
img = Image.open('caffee.png')
# img = Image.open(r'C:\Users\s.horiuchi\Documents\Python\auto\caffee.png')
print(f'ファイル名： {img.filename}, フォーマット：{img.format}, サイズ： {img.size}')