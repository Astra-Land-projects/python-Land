from PIL import Image

class ImageRotator:

    def rotate(self, image_path, angle):
        image = Image.open(image_path)
        image.rotate(angle, expand=True).save("rotated_" + image_path)
        print("Done.")