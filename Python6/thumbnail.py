from PIL import Image

class ThumbnailCreator:

    def create(self, image_path):
        image = Image.open(image_path)
        image.thumbnail((200, 200))
        image.save("thumb_" + image_path)
        print("Done.")