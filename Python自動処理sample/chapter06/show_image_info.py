from PIL import Image
img = Image.open('caffee.png')
print(f'ファイル名: {img.filename}, フォーマット: {img.format}, サイズ: {img.size}')
