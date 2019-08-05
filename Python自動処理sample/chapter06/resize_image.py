from PIL import Image
img = Image.open('caffee.png')
resized_img = img.resize((200, 200))
resized_img.save('caffee_small.png')
