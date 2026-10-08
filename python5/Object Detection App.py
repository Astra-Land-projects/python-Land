from ultralytics import YOLO

model = YOLO("yolo11n.pt")

image = input("Image: ")

results = model(image)

for result in results:

    for box in result.boxes:

        cls = int(box.cls[0])
        confidence = float(box.conf[0])

        name = result.names[cls]

        print(
            f"{name}: "
            f"{confidence:.2f}"
        )