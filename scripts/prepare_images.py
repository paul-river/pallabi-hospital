from PIL import Image, ImageDraw
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'source-images'
DEST=ROOT/'site/assets/images'
ORIG=ROOT/'source-images'
DEST.mkdir(parents=True,exist_ok=True)
ORIG.mkdir(parents=True,exist_ok=True)
for i in range(1,16):
    file=SRC/f'Hospital Images ({i}).jpeg'
    img=Image.open(file).convert('RGB')
    if img.width>1300: img.thumbnail((1300,1300),Image.Resampling.LANCZOS)
    img.save(DEST/f'hospital-{i:02d}.webp','WEBP',quality=82,method=6)
for key,name in [('chairman','Chairman.jpeg'),('ceo','CEO.jpeg'),('managing-director','Managing Director.jpeg'),('director','Director.jpeg')]:
    file=SRC/name
    img=Image.open(file).convert('RGB')
    img.thumbnail((1000,1400),Image.Resampling.LANCZOS)
    img.save(DEST/f'{key}.webp','WEBP',quality=85,method=6)
logo=Image.open(SRC/'Logo.jpeg').convert('RGBA')
# Keep the official circular emblem while removing the checkerboard background around it.
w,h=logo.size
bbox=(round(w*.045),round(h*.045),round(w*.955),round(h*.955))
logo=logo.crop(bbox)
S=logo.width
mask=Image.new('L',(S,S),0)
draw=ImageDraw.Draw(mask)
draw.ellipse((1,1,S-2,S-2),fill=255)
logo.putalpha(mask)
logo.thumbnail((520,520),Image.Resampling.LANCZOS)
logo.save(DEST/'logo.png',optimize=True)
logo.resize((64,64),Image.Resampling.LANCZOS).save(ROOT/'site/favicon.png',optimize=True)
print('Prepared 20 images and favicon')
