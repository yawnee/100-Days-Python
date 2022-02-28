from selenium import webdriver

chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.python.org/')

## My solution ############################################
menu = driver.find_element_by_xpath("/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")
menu = menu.text
menu = menu.split("\n")

menu_dict = {menu[i]: menu[i + 1] for i in range(0, len(menu), 2)}

for each_day in menu_dict:
    print(f'{each_day}: {menu_dict[each_day]}')
#############################################################

