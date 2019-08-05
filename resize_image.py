from PIL import Image

img = Image.open('caffee.png')
# img = Image.open(r'C:\Users\s.horiuchi\Documents\Python\auto\caffee.png')
resized_img = img.resize((200, 200))
resized_img.save('caffee_small.png')