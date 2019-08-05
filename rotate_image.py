from PIL import Image

img = Image.open('caffee.png')
# img = Image.open(r'C:\Users\s.horiuchi\Documents\Python\auto\caffee.png')
rotated_img = img.rotate(90)
rotated_img.save('caffee_rotated.png')