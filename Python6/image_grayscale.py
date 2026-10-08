from PIL import Image

class ImageGrayScale:

    def convert(self, image_path):
        image = Image.open(image_path)
        image = image.convert("L")
        image.save("gray_" + image_path)
        print("Done.")