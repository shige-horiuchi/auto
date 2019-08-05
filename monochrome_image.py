from PIL import Image

img = Image.open('caffee.png')
# img = Image.open(r'C:\Users\s.horiuchi\Documents\Python\auto\caffee.png')
monochrome_img = img.convert('L')
monochrome_img.save('caffee_monochrome.png')