from PIL import Image

img = Image.open('caffee.png')
# img = Image.open(r'C:\Users\s.horiuchi\Documents\Python\auto\caffee.png')
cropped_img = img.crop(box = (0, 0, 500, 500))
cropped_img.save('caffee_cropped.png')