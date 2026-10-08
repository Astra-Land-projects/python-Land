import cv2

image_path = input("Image: ")

image = cv2.imread(image_path)

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

faces = face_detector.detectMultiScale(
    gray,
    1.1,
    5
)

for i, (x, y, w, h) in enumerate(faces):

    face = gray[y:y+h, x:x+w]

    cv2.imwrite(
        f"emotion_input_{i}.jpg",
        face
    )

    print(
        f"Face {i}: "
        "ready for emotion model"
    )