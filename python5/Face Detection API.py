import cv2

image_path = input("Image: ")

image = cv2.imread(image_path)

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

faces = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

print("Faces:", len(faces))

for i, (x, y, w, h) in enumerate(faces):

    face = image[
        y:y+h,
        x:x+w
    ]

    cv2.imwrite(
        f"face_{i}.jpg",
        face
    )