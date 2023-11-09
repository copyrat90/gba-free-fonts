from bmtext.pil import BMText
from bmtext.meta import parse_file
from PIL import Image

fnt_path = "fusion-pixel-font-10.fnt"

cell_width = 16
cell_height = 16

grid_width = 256
grid_height = 256

img_width = cell_width * grid_width
img_height = cell_height * grid_height

im = Image.new("RGB", (img_width, img_height), color=(0,0,0))
drawer = BMText(im)
font = parse_file(fnt_path)

f = open(fnt_path, "r")
for i in range(3):
    f.readline()


chars_count = int(f.readline().split(" ")[1].split("=")[1])

print(chars_count)

for i in range(chars_count):
    num = int(f.readline().split(" ")[1].split("=")[1])
    utf_idx = num - 32
    drawer.text((cell_width * (utf_idx % grid_width), cell_height * (utf_idx // grid_width)), chr(num), font, fill="white")
    if i % 1000 == 0:
        print(i)

im.save("converted_font.png")
f.close()
