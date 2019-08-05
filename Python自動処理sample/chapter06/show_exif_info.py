from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('./IMG_0266.JPG')
exif = img._getexif()
if exif is None:
  print("EXIF情報がありません")
else:
  for tagID, tagValue in exif.items():
    tagName = TAGS[tagID]
    print(tagName, tagValue)
