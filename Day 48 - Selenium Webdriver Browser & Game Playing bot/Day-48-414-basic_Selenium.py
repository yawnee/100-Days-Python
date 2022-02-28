from selenium import webdriver

chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    "https://www.amazon.ca/Soundcore-Cancelling-Headphones-Comfortable-Bluetooth/dp/B08HMWZBXC/?_encoding=UTF8&pd_rd_w=IPZaM&pf_rd_p=b926dfe5-e736-4fbf-860e-045028750ff9&pf_rd_r=51JJ6KBQQA99FMZAEBHP&pd_rd_r=90ef2b92-c379-4cd6-9679-10bc55d57fed&pd_rd_wg=soAEi&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
price = driver.find_element_by_class_name("a-price-whole")
print(price.text)

search = driver.find_element_by_name('site-search')
print(search.tag_name)

logo = driver.find_element_by_id("nav-logo-sprites")
print(logo.size)

# logo_link = driver.find_element_by_css_selector("nav-logo a")
# print(logo_link.text)

review_rating = driver.find_element_by_xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr[6]/td')
print(review_rating.text)


# Closes the tab
# driver.close()

# Closes the browser
# driver.quit()
