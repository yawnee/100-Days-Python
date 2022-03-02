from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\5onic\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Profile 1')  # e.g. Profile 3
chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
# driver.get('https://www.pof.com/meetme')
driver.get('https://www.okcupid.com/home')

# Give some time to load up the page
time.sleep(6)
#Male version:
like_button = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/button')
# Female Version:
#like_button = driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/button')


def daily_likes_timeout():
    try:
        # male version of timeout?
        daily_likes = driver.find_element_by_xpath('//*[@id="OkModalContent-main"]/div[2]/div/div[2]/div')
        #daily_likes = driver.find_element_by_xpath('//*[@id="OkModalContent-main"]/div[2]/div/div[1]/div/div')
        hour = daily_likes.text.split(' ', 1)[0]
        seconds = int(hour.split('h', 1)[0]) * 60 * 60
        print(hour, seconds)
        print(daily_likes.text)
        time.sleep(seconds)
    except NoSuchElementException:
        return False

def profile():
    try:
        name = driver.find_element_by_class_name('card-content-header__text')
        description = driver.find_element_by_class_name('dt-essay-text')
        print(f'You liked: {name.text}')
        print(f'Their profile are: {description.text}')
        time.sleep(2)
    except NoSuchElementException:
        like_button.click()


def matched():
    try:
        exit_click = driver.find_element_by_class_name("okicon i-close")
        exit_click.click()
    except:
        return False

time.sleep(3)
while True:
    print("")
    if daily_likes_timeout:
        time.sleep(2)
        daily_likes_timeout()

    try:
        like_button.click()
    except NoSuchElementException:
        profile()

    if matched:
        matched()









    #     try:
    #         name = driver.find_element_by_class_name('card-content-header__text')
    #         description = driver.find_element_by_class_name('dt-essay-text')
    #         print(f'You liked: {name.text}')
    #         print(f'Their profile are: {description.text}')
    #         #like_button.click()
    #         time.sleep(2)
    #     except NoSuchElementException:
    #         like_button.click()
    #         time.sleep(1)
    # except NoSuchElementException:
    #     exit_click = driver.find_element_by_class_name("okicon i-close")
    #     exit_click.click()
    #     time.sleep(10)
    # else:
    #     like_button.click()
    #     time.sleep(1)

# while True:
#     print("")
#     time.sleep(1)
#     try:
#         exit_click = driver.find_element_by_class_name("okicon i-close")
#         exit_click.click()
#         time.sleep(10)
#     except NoSuchElementException:
#         try:
#             name = driver.find_element_by_class_name('card-content-header__text')
#             description = driver.find_element_by_class_name('dt-essay-text')
#             print(f'You liked: {name.text}')
#             print(f'Their profile are: {description.text}')
#             like_button.click()
#             time.sleep(2)
#         except NoSuchElementException:
#             try:
#                 like_button.click()
#                 time.sleep(1)
#             except ElementClickInterceptedException:
#                 time.sleep(5)
#             else:
#                 pass
#     else:
#         like_button.click()
#         time.sleep(1)
