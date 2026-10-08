from PIL import Image

chars = "@%#*+=-:. "
path = input("Image file: ").strip()

img = Image.open(path).convert("L")
img = img.resize((80, int(img.height * 80 / img.width * 0.5)))

for y in range(img.height):
    line = ""
    for x in range(img.width):
        p = img.getpixel((x, y))
        line += chars[p * len(chars) // 256]
    print(line)