import pyautogui


class Screenshot:

    def capture(self):
        image = pyautogui.screenshot()
        image.save("screenshot.png")
        print("Screenshot Saved.")