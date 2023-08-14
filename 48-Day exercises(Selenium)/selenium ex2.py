from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(number.text)

# 2nd way
number2 = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(number2.text)