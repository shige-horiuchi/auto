from pathlib import Path
from PIL import Image

box_size = 500
input_folder = Path('images')
output_folder = Path('resize_fill_box')
output_folder.mkdir(exist_ok=True)

for f in input_folder.glob('*.png'):
  img = Image.open(f)
  width, height = img.size
  ratio = box_size / min(img.size)
  resized_img = img.resize((int(width * ratio), int(height * ratio)))
  if width > height:
    strip_size = resized_img.size[0] - box_size
    cropped_img = resized_img.crop((
      strip_size / 2,
      0,
      resized_img.size[0] - strip_size / 2,
      resized_img.size[1]
  ))
  else:
    strip_size = resized_img.size[0] - box_size
    cropped_img = resized_img.crop((
      0,
      strip_size / 2,
      resized_img.size[0],
      resized_img.size[1] - strip_size / 2
  ))
  save_path = output_folder.joinpath(f.name)
  cropped_img.save(save_path)
  img.close()
