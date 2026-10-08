from selenium import webdriver

class WebsiteScreenshot:

    def capture(self, url):
        driver = webdriver.Chrome()

        driver.get(url)

        driver.save_screenshot("website.png")

        driver.quit()

        print("Screenshot Saved.")