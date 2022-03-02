from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://secure-retreat-92358.herokuapp.com/')

# article_count = driver.find_element_by_css_selector("#articlecount a")
# #article_count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# #all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Inserting credentials on a form
# You need to find the <input> HTML
first_name = driver.find_element_by_name("fName")
first_name.send_keys("john")
second_name = driver.find_element_by_name("lName")
second_name.send_keys("doe")
email = driver.find_element_by_name("email")
email.send_keys("john.doe@johnnytest.com")
submit = driver.find_element_by_class_name("btn") # OR driver.find_element_by_css_selector("form button")
submit.click()
