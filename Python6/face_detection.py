import cv2


class FaceDetection:

    def run(self):
        detector = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        camera = cv2.VideoCapture(0)

        while True:
            _, frame = camera.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow("Face Detection", frame)

            if cv2.waitKey(1) == ord("q"):
                break

        camera.release()
        cv2.destroyAllWindows()