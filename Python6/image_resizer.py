from PIL import Image

class ImageResizer:

    def resize(self, image_path, width, height):
        image = Image.open(image_path)
        image = image.resize((width, height))
        image.save("resized_" + image_path)
        print("Done.")