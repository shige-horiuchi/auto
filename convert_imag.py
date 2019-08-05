from PIL import Image
img = Image.open('caffee.png')
# img = Image.open(r'C:\Users\s.horiuchi\Documents\Python\auto\caffee.png')
img.save('caffee.jpg', format = 'jpeg')