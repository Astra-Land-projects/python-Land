import cv2


class Webcam:

    def start(self):
        camera = cv2.VideoCapture(0)

        while True:
            success, frame = camera.read()

            if not success:
                break

            cv2.imshow("Webcam", frame)

            if cv2.waitKey(1) == ord("q"):
                break

        camera.release()
        cv2.destroyAllWindows()