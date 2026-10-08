from PIL import Image

path = input("Image file: ").strip()
w = int(input("Width: "))
h = int(input("Height: "))

img = Image.open(path)
img = img.resize((w, h))
out = "resized_" + path
img.save(out)
print("Saved:", out)