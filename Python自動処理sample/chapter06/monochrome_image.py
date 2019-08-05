from PIL import Image
img = Image.open('caffee.png')
monochrome_img = img.convert('L')
monochrome_img.save('caffee_monochrome.png')
