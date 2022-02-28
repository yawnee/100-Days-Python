from selenium import webdriver
import time

chrome_driver_path = r"..\Day 00 - Development Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# Time
# timeout = time.time() + 5
# five_min = time.time() + 60*5 # 5minutes

# #Click Perks
# buyCursor = driver.find_element_by_id("buyCursor")
# cost_buyCursor = driver.find_element_by_css_selector('/html/body/div[3]/div[5]/div/div[1]/b/text()[2]')
# print(cost_buyCursor.text)
# cost_buyGrandma = driver.find_element_by_id('/html/body/div[3]/div[5]/div/div[2]/b/text()[2]')
# print(cost_buyGrandma.text)
# # buyGrandma = driver.find_element_by_id("buyGrandma")
# # buyFactory = driver.find_element_by_id("buyFactory")
# # buyFactory = driver.find_element_by_id("buyFactory")
# # buyMine = driver.find_element_by_id("buyMine")
# # buyMine = driver.find_element_by_id("buyMine")
# # buyShipment = driver.find_element_by_id("buyShipment")
# # buyShipment = driver.find_element_by_id("buyShipment")
# # buyAlchemy = driver.find_element_by_id("buyAlchemy lab")
# # buyAlchemy = driver.find_element_by_id("buyAlchemy lab")
# # buyPortal = driver.find_element_by_id("buyPortal")
# # buyPortal = driver.find_element_by_id("buyPortal")
# # buyTime = driver.find_element_by_id("buyTime machine")
# # buyTime = driver.find_element_by_id("buyTime machine")
#
# #Current Cookies
# money = driver.find_element_by_id("money")
# print(money.text)
#
# #When class is not "grayed" (it means the perk cannot be purchased)
#
#
# count = 0
#
#
# while count <= 101:
#     cookie = driver.find_element_by_id("cookie")
#     cookie.click()
#     count = count + 1
#
# print(money.text)


# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break