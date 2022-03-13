from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os

PROFILE = os.environ.get('PROFILE')

options = webdriver.ChromeOptions()
options.add_argument(fr"--user-data-dir=C:\Users\{PROFILE}\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Profile 1')  # e.g. Profile 3
chrome_driver_path = Service(r"..\Day 00 - Development Tools\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=options)
driver.get('https://www.okcupid.com/home')


def click_like():
    try:
        like_button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label'
                                                                                                      '=LIKE]')))
        print(f'like button was found, OK: {like_button.size}')
        like_button.click()
    except:
        print('Like button was KO, error')
        pass


def intro():
    import random

    try:
        intro_button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label'
                                                                                                       '=INTRO]')))
        print(f'intro button was found, OK: {intro_button.size}')
        intro_button.click()
    except:
        print('intro button was KO, error')
        pass

    try:
        new_intro_button_location = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dt-comment-fab')))
        print(f'intro button was found, OK: {new_intro_button_location.size}')
        new_intro_button_location.click()
    except:
        print('new intro button location not found, KO, error')
        pass

    try:
        intro_send = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'BxLIffwavFC1udtULr_8')))
        intro_send_click = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'BxLIffwavFC1udtULr_8')))

        with open('jokes.txt', mode='r') as file:
            joke_list = file.readlines()
            random_message = random.choice(joke_list)
        print(random_message)
        intro_send_click.click()
        intro_send.send_keys(random_message)
        print('Intro message sent, OK: ')
    except:
        print('intro send was KO, error')
        pass

    try:
        send_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'pnbgZN7izvYY_0kDp1Rk')))
        send_button.click()
    except:
        print('SEND button was KO, error')
        pass


def daily_likes_timeout():
    try:
        daily_likes_timer = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'formatted-countdown')))
        hours = daily_likes_timer.text.split(' ', 1)[0]
        hours = int(hours.split('h', 1)[0])
        minutes = daily_likes_timer.text.split(' ', 1)[1]
        minutes = int(minutes.split('m', 1)[0])
        print(f'Hr: {hours}, Min: {minutes}')
        print(daily_likes_timer.text)
        if hours == 0:
            delay_seconds = minutes * 60
            print(f'Time Remaining: {delay_seconds}')
            time.sleep(delay_seconds)
        elif minutes == 0 and minutes == 0:
            delay_seconds = 59
            time.sleep(delay_seconds)
        else:
            delay_seconds = hours * 60 * 60
            print(f'Time Remaining: {delay_seconds}')
            time.sleep(delay_seconds)

    except:
        print('Daily likes is KO')
        return False


def profile():
    try:
        name = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card-content-header__text')))
        description = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'dt-essay-text')))
        print(f'You liked: {name.text}')
        print(f'Their profile are: {description.text}')
    except (NoSuchElementException, TimeoutException):
        print('Profile is KO, error')
        return False


def matched():
    try:
        exit_click = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'connection-view-container-close-button')))
        print(f'Close button was found: {exit_click.size}')
        exit_click.click()
        print('Match window was successfully closed')
    except:
        print('Match window was not closed, KO, error:')
        return False


while True:
    print("")
    matched()
    profile()
    intro()
    daily_likes_timeout()
    matched()
