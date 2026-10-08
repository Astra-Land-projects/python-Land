from PIL import Image
import os

class ImageConverter:

    def convert(self, image_path, fmt):
        image = Image.open(image_path)
        name = os.path.splitext(image_path)[0]
        image.save(f"{name}.{fmt}")
        print("Converted.")