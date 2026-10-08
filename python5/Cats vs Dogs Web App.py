import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model(
    "cats_dogs_model.keras"
)

path = input("Image: ")

img = Image.open(path).convert("RGB")
img = img.resize((150, 150))

x = np.array(img) / 255.0
x = np.expand_dims(x, axis=0)

prediction = model.predict(x)[0][0]

if prediction > 0.5:
    print("Dog")
else:
    print("Cat")