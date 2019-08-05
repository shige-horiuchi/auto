from pathlib import Path
from PIL import Image

input_folder = Path('images')
output_folder = Path('exif_removed')
output_folder.mkdir(exist_ok=True)

for f in input_folder.glob('*.jpg'):
    img = Image.open(f)
    save_path = output_folder.joinpath(f.name)
    img.save(save_path)
    img.close()
