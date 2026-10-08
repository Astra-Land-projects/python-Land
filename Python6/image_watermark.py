from PIL import Image, ImageDraw

class ImageWatermark:

    def add_watermark(self, image_path, text):
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        draw.text((20, 20), text)

        image.save("watermarked_" + image_path)
        print("Done.")