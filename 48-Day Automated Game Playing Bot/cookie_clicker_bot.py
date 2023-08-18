import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds
    if time.time() > timeout:
        money = driver.find_element(By.ID, "money")
        cookies_count = int(money.text.replace(",", ""))

        grandma = driver.find_element(By.ID, "buyGrandma")
        factory = driver.find_element(By.ID, "buyFactory")
        mine = driver.find_element(By.ID, "buyMine")
        shipment = driver.find_element(By.ID, "buyShipment")
        alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
        portal = driver.find_element(By.ID, "buyPortal")
        time_machine = driver.find_element(By.ID, "buyTime machine")

        # Checks whether cookies enough to buy something(granny, factory, mine, etc.)
        if cookies_count >= int(str(driver.find_element(By.ID, "buyTime machine").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            time_machine.click()
        elif cookies_count >= int(str(driver.find_element(By.ID, "buyPortal").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            portal.click()
        elif cookies_count >= int(str(driver.find_element(By.ID, "buyAlchemy lab").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            alchemy_lab.click()
        elif cookies_count >= int(str(driver.find_element(By.ID, "buyShipment").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            shipment.click()
        elif cookies_count >= int(str(driver.find_element(By.ID, "buyMine").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            mine.click()
        elif cookies_count >= int(str(driver.find_element(By.ID, "buyFactory").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            factory.click()
        elif cookies_count >= int(str(driver.find_element(By.ID, "buyGrandma").text).split("-")[1].strip().split("\n")[0].replace(",", "")):
            grandma.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break



