from PIL import Image

class ImageToPDF:

    def convert(self, image_path, output):
        image = Image.open(image_path).convert("RGB")
        image.save(output)
        print("Done.")