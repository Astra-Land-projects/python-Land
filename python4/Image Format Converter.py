from PIL import Image

path = input("Image file: ").strip()
fmt = input("Format (png/jpg/webp): ").strip().lower()

img = Image.open(path)
out = path.rsplit(".", 1)[0] + "." + fmt
img.save(out)
print("Saved:", out)