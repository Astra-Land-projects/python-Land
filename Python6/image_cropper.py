from PIL import Image

class ImageCropper:

    def crop(self, image_path, left, top, right, bottom):
        image = Image.open(image_path)
        image.crop((left, top, right, bottom)).save("cropped_" + image_path)
        print("Done.")