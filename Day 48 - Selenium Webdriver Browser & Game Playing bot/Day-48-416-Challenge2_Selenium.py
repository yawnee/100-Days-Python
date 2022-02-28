from selenium import webdriver

chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

## My solution 1 ############################################
num_of_articles = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
articles = num_of_articles.text
print(articles)
# #############################################################

## My solution 2 ############################################
num_of_articles = driver.find_element_by_css_selector("#articlecount a")
articles = num_of_articles.text
print(articles)