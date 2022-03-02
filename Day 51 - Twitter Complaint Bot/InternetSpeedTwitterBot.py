import time
from selenium import webdriver

PROMISED_DOWN = 240
PROMISED_UP = 100


class InternetSpeedTwitterBot:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"--user-data-dir=C:\Users\YOUR_PROFILE_NAME_HERE\AppData\Local\Google\Chrome\User Data")
        self.options.add_argument(r'--profile-directory=Profile 1')  # e.g. Profile 3
        self.chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, chrome_options=self.options)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        start = self.driver.find_element_by_class_name('start-text')
        start.click()
        print('speedtest started')
        time.sleep(50)
        download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        download = download.split(".", 1)[0]
        print(download)
        download = int(download)

        upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        upload = upload.split(".", 1)[0]
        print(upload)
        upload = int(upload)

        if PROMISED_DOWN <= download or PROMISED_UP <= upload:
            return True
        else:
            return False

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        time.sleep(5)
        input = self.driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']/div/div/div/span")
        input.send_keys("My internet speeds are below advertised!")
        button = self.driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']")
        button.click()
