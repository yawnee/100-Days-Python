from selenium import webdriver
import time

chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://orteil.dashnet.org/experiments/cookie/')
